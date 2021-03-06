import time
from lxml import etree
from PyQt5.QtCore import QThread, pyqtSignal
import random
from constant import *
from urllib import request
from bs4 import BeautifulSoup
import utils
from utils import mutex
from mysql_model import *
from dialog import WebViewDialog
# 自动化引入
# ###超时相关
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
# ###设备相关
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class Worker(QThread):
    sinOut = pyqtSignal(str)  # 自定义信号，执行run()函数时，从相关线程发射此信号
    crawler_progress = pyqtSignal(int, int)  # 爬虫进度条信号
    details_progress = pyqtSignal(int, int)  # 详情爬虫进度条信号
    chapter_progress = pyqtSignal(int, int)  # 章节进度条信号
    crawler_chapter_progress = pyqtSignal(int, int)  # 爬取章节进度条信号
    message_box = pyqtSignal(str, str)  # 弹窗提示
    execution_method = pyqtSignal(str)  # 执行方法
    change_full_control_status = pyqtSignal(bool)  # 改变全部控件状态
    data_info_table = pyqtSignal(dict)  # 数据表格

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.type = None
        self.db_session = None
        self.working = True
        self.db_connect = None
        # 是否断点续爬
        self.item_bank_continue = False
        self.subject_code = ''
        self.from_code = ''
        self.subject_name = ''
        self.teaching = ''
        self.teaching_name = ''
        self.level_code = ''
        self.level_name = ''
        self.chapter_id = ''
        self.is_recursive = False  # 是否递归
        self.cookies = dict()
        self.num = 0
        self.crawl_maximum = 0
        self.driver = None
        self.UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari\
        /537.36'
        self.phantomjs_path = utils.get_phantomjs_path()
        self.desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
        self.cookie_dict = {
            'name': '',
            'value': '',
            'domain': '.jyeoo.com',
            'path': '/',
            'expiry': int(time.time()) + 10000000
        }

    def __del__(self):
        self.working = False
        self.wait()
        self.driver.close()
        self.driver.quit()

    def init_phantomjs_driver(self):

        # get()方法会一直等到页面被完全加载，然后才会继续程序
        headers = {'Accept': '*/*',
                   'Accept-Language': 'en-US,en;q=0.8',
                   'Cache-Control': 'max-age=0',
                   'User-Agent': self.UA,
                   'Connection': 'keep-alive',
                   }
        for key, value in headers.items():
            self.desired_capabilities['phantomjs.page.customHeaders.{}'.format(key)] = value

        self.desired_capabilities[
            'phantomjs.page.customHeaders.User-Agent'] = self.UA
        self.driver = webdriver.PhantomJS(executable_path=self.phantomjs_path,
                                          desired_capabilities=self.desired_capabilities)
        # 设置超时时间30秒
        self.driver.set_page_load_timeout(30)

    def add_cookie(self):
        for k, v in self.cookies.items():
            self.cookie_dict['name'] = k
            self.cookie_dict['value'] = v
            self.driver.add_cookie(self.cookie_dict)

    def set_button_enabled(self, status):
        """
        批量设置按钮状态
        :param status: True/False
        :return:
        """
        self.change_full_control_status.emit(status)

    def run(self):

        # 禁用按钮
        self.set_button_enabled(False)
        if not self.driver:
            self.init_phantomjs_driver()
        # 发出信号
        self.sinOut.emit("无头浏览器启动完成")
        # 添加cookie
        self.add_cookie()
        if self.type:
            try:
                # 动态执行方法
                eval('self.{func}()'.format(func=self.type))
            except Exception as e:
                # 出现错误！
                self.sinOut.emit(str(e))
                image_png = self.driver.get_screenshot_as_png()
                self.driver.get_screenshot_as_file('./error.png')
                # wvd = WebViewDialog()
                # wvd.set_image(image_png)
                # wvd.exec_()
                with open('error.html', 'w') as error_file:
                    error_file.write(self.driver.page_source)

            finally:
                # self.driver.close()
                # 启用按钮
                self.set_button_enabled(True)

    def get_pointcard(self, fieldset_id, bank_item, et):
        """
        获取知识点
        :param fieldset_id:
        :param bank_item:
        :param et:
        :return:
        """
        chaper_id = bank_item.get('chaper_id')
        pointcard_xpath = et.xpath('//div[@class="pt3"]')
        if not pointcard_xpath:
            pass
            return
        point_a = pointcard_xpath[0].xpath('.//a')
        result = list()
        for item in point_a:
            onclick = item.xpath('./@onclick')
            if not onclick:
                continue
            onclick = onclick[0].split(';')[0].split('openPointCard')[1]
            onclick = onclick.replace("'", "").replace('"', '').replace('(', "").replace(")", "")
            pointcard = onclick.split(',')

            pointcard_page = POINTCARD_PAGE.format(subject=pointcard[0],
                                                   point_code=pointcard[1])
            self.sinOut.emit('正在爬取知识点信息页  %s' % pointcard_page)
            retry_count = 0
            while True:
                html = request.urlopen(pointcard_page + '&r=' + str(random.random()))
                download_soup = BeautifulSoup(html, 'lxml')
                title = download_soup.find('b')
                if not title and retry_count < 3:
                    retry_count += 1
                    continue
                if title:
                    title = title.text
                break
            item_point = dict(url=pointcard_page,
                              item_id=fieldset_id,
                              code=pointcard[1],
                              subject=pointcard[0],
                              chaper_id=chaper_id,
                              title=title,
                              content=download_soup)
            result.append(item_point)
        return result

    def item_bank_deails_and_point_db(self, bank_item):
        """
        详情页入库
        :param bank_item:
        :return:
        """
        points = bank_item.pop('points')
        for point in points:
            # 课题知识点
            if self.db_connect.session.query(ItemPoint).filter(ItemPoint.item_id == point['item_id'],
                                                               ItemPoint.point_code == point['code']).count() == 0:
                self.db_connect.add(ItemPoint(**dict(
                    item_id=point['item_id'],
                    point_code=point['code']
                )))
            # 章节知识点
            if self.db_connect.session.query(ChaperPoint).filter(ChaperPoint.chaper_id == point['chaper_id'],
                                                                 ChaperPoint.code == point['code']).count() == 0:
                self.db_connect.add(ChaperPoint(**dict(chaper_id=point['chaper_id'],
                                                       title=point['title'],
                                                       code=point['code'],
                                                       content=str(point['content']),
                                                       url=point['url'])))
        # 课题入库
        self.db_connect.add(ItemBank(**bank_item))
        return

    def item_bank_details(self):
        """
        详情页爬取方法
        :return:
        """
        current_count = 0
        if not self.chapter_id:
            self.sinOut.emit('错误！章节获取失败，可能未选择章节！')
        else:
            start_urls = self.get_details_url()
            for item in start_urls:
                current_count += 1
                bank_item = dict()
                self.sinOut.emit('正在获取详情页 %s' % item.get('detail_page_url'))
                self.driver.get(item.get('detail_page_url'))
                et = etree.HTML(self.driver.page_source)
                year_html = et.xpath('.//div[@class="pt1"]/a/text()')
                if year_html:
                    year_area = utils.txt_wrap_by('（', '）', year_html[0])
                    if not year_area:
                        year_area = utils.txt_wrap_by('(', ')', year_html[0])
                    if year_area:
                        bank_item['year_code'] = year_area.split('•')[0]
                    bank_item['year_area'] = year_area
                else:
                    bank_item['year_area'] = ''
                bank_item['used_times'] = ''
                bank_item['exam_times'] = ''
                fieldset_xpath = '//div[@id="{fieldset_id}"]'.format(fieldset_id=item.get('fieldset_id'))
                detail_data = et.xpath(fieldset_xpath)
                # 考题
                bank_item['context'] = str(detail_data[0].xpath('.//div[@class="pt1"]/text()'))
                bank_item['anwser'] = self.driver.page_source
                fieldtip_left = detail_data[0].xpath('.//div[@class="fieldtip-left"]')
                record_time = fieldtip_left[0].xpath('.//span[1]/text()')
                used_times = fieldtip_left[0].xpath('.//span[2]/text()')
                exam_times = fieldtip_left[0].xpath('.//span[3]/text()')
                difficult_code = fieldtip_left[0].xpath('.//span[4]/text()')
                if record_time:
                    bank_item['record_time'] = record_time[0].replace("：", ":").split(':')[1]
                if used_times:
                    bank_item['used_times'] = used_times[0].replace("：", ":").split(':')[1]
                if exam_times:
                    bank_item['exam_times'] = exam_times[0].replace("：", ":").split(':')[1]
                if difficult_code:
                    bank_item['difficult_code'] = difficult_code[0].replace("：", ":").split(':')[1]
                bank_item['from_code'] = self.from_code
                bank_item['url'] = item.get('detail_page_url')
                bank_item['chaper_id'] = item.get('chaper_id')
                bank_item['library_id'] = item.get('library_id')
                bank_item['item_style_code'] = item.get('item_style_code')
                point_list = self.get_pointcard(item.get('fieldset_id'), bank_item, et)
                bank_item['points'] = point_list
                # 入库
                mutex.acquire()
                self.item_bank_deails_and_point_db(bank_item)
                mutex.release()
                # 更新爬虫次数进度
                self.details_progress.emit(current_count, int(self.crawl_maximum))

        return

    @staticmethod
    def update_chapter_pk_id(old_chapters_id, pk, chapters_list):
        """
        更新章节数据中的全部id
        :param old_chapters_id:
        :param pk:
        :param chapters_list:
        :return:
        """
        relational_dict = dict()
        for item in chapters_list:
            if item.get('pk') == pk:
                relational_dict[item['id']] = old_chapters_id
                item['id'] = old_chapters_id
        for item in chapters_list:
            if item.get('parent_id'):
                item['parent_id'] = relational_dict.get(item['parent_id'])
        return chapters_list

    def library_chapter(self):
        """
        章节爬取动作
        :return:
        """
        start_url = self.get_chapter_url()
        try:
            self.driver.get(start_url)
            WebDriverWait(self.driver, 30).until(
                ec.visibility_of_element_located((By.XPATH, '//div[@class="tree-head"]/span[@id="spanEdition"]')))
        except TimeoutException as e:
            self.sinOut.emit('超时！！！ %s' % str(e))
            self.driver.get_screenshot_as_file('./error.png')
            return
        teaching = self.driver.find_element_by_xpath('//div[@class="tree-head"]/span[@id="spanEdition"]').text
        level_name = self.driver.find_element_by_xpath('//div[@class="tree-head"]/span[@id="spanGrade"]').text
        teaching = teaching.replace(':', '').replace('：', '')
        self.sinOut.emit('进行爬取章节！')
        if self.teaching_name != teaching or self.level_name != level_name:
            self.message_box.emit('警告', "没有数据！")
            return
        et = etree.HTML(self.driver.page_source)
        library_id = self.teaching
        sub_obj = et.xpath('//ul[@id="JYE_POINT_TREE_HOLDER"]/li')
        chapters_list = list()

        total = len(sub_obj)
        current_count = 0
        for item in sub_obj:
            lc_item = dict()
            lc_item['id'] = str(uuid.uuid1())
            pk = item.attrib.get('pk')
            nm = item.attrib.get('nm')
            child = utils.recursive_get_li(lc_item['id'], library_id, item)
            lc_item['pk'] = pk
            lc_item['parent_id'] = ''
            lc_item['library_id'] = library_id
            lc_item['name'] = nm
            lc_item['child'] = child
            chapters_list.append(lc_item)
            current_count += 1
            self.crawler_chapter_progress.emit(current_count, total)
        self.sinOut.emit('正在解析入库')

        if chapters_list:
            mutex.acquire()
            chapters = self.db_connect.session.query(LibraryChapter.name, LibraryChapter.id, LibraryChapter.pk).filter(
                LibraryChapter.library_id == library_id)
            new_list = utils.split_list(chapters_list)
            if chapters.count() > 0:
                # 如果章节存在数据则进行更新
                relational_dict = dict()
                for item in chapters:
                    # new_list = self.update_chapter_pk_id(item.id, item.pk, new_list)
                    for item2 in new_list:
                        if item2.get('pk') == item.pk:
                            relational_dict[item2['id']] = item.id
                            item2['id'] = item.id
                            break
                    for item3 in new_list:
                        if item3.get('parent_id') and relational_dict.get(item3['parent_id']):
                            item3['parent_id'] = relational_dict.get(item3['parent_id'])
                chapters.delete()
                self.db_connect.session.commit()
            mutex.release()

            # 插入新值
            for item in new_list:
                mutex.acquire()
                if 'child' in item:
                    del item['child']
                self.db_connect.add(LibraryChapter(**item))
                mutex.release()
        self.sinOut.emit('章节爬取完成，重新加载查看')

    def item_bank(self):
        """
        题库爬取动作
        :return:
        """
        start_url = self.get_item_bank_init_url(self.chapter_id, self.subject_code)
        for chapters in start_url:
            for item in chapters.values():
                try:
                    self.driver.get(item.get('url'))
                    # 滚动页面
                    self.driver.execute_script('window.scrollBy(0, 1000)')
                    # 翻页入库
                    self.page_turning(item)
                except Exception as e:
                    # 出现错误！
                    self.sinOut.emit(str(e))
                    image_png = self.driver.get_screenshot_as_png()
                    self.driver.get_screenshot_as_file('./error.png')
                    wvd = WebViewDialog()
                    wvd.set_image(image_png)
                    wvd.exec_()

    def page_turning(self, args):
        """
        翻页入库
        :param args:
        :return:
        """
        # 获取总题量
        WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located((By.XPATH, '//td[@id="TotalQuesN"]/em')))
        topic_count = self.driver.find_element_by_xpath('//td[@id="TotalQuesN"]/em').text
        # 已经爬取的个数
        already_crawler_count = 0
        while True:

            # 等待翻页已加载到页面
            WebDriverWait(self.driver, 30).until(
                ec.visibility_of_element_located((By.XPATH, "//a[@class='index cur']")))

            # 获取当前页
            cur_page = self.driver.find_element_by_xpath('//a[@class="index cur"]').text
            # 获取总页数
            total_pages = 0
            one_page = self.driver.find_element_by_xpath('//select[@class="ml10"]/option[@value="1"]').text
            if one_page:
                total_pages = one_page.split('/')[1].lstrip()
            # 下一页
            next_page = int(cur_page) + 1
            # 更新爬虫次数进度
            self.crawler_progress.emit(next_page, int(self.crawl_maximum))
            # 更新章节进度条
            self.chapter_progress.emit(already_crawler_count, int(topic_count))
            # 判断是否完成章节的爬取
            if already_crawler_count >= int(topic_count):
                self.sinOut.emit("已经爬取完章节题数： %s 【结束】" % str(already_crawler_count))
                break
            if next_page > int(total_pages):
                # 判断是否是最后一页
                # 如果下一页 大于 总页数 则跳出循环
                self.sinOut.emit(
                    "已经爬取完 {cur_page} / {total_pages} 【结束】".format(cur_page=cur_page, total_pages=total_pages))
                break

            fieldset = self.driver.find_elements_by_xpath('.//fieldset')
            for item in fieldset:
                fieldset_id = item.get_attribute('id')

                if not fieldset_id or fieldset_id == '00000000-0000-0000-0000-000000000000':
                    self.sinOut.emit("错误！题目的id错误")
                    continue
                detail_page_url = DETAIL_PAGE.format(subject=self.subject_code, fieldset=fieldset_id)
                # print(detail_page_url)
                # 入库
                self.add_chapter_to_db(fieldset_id, detail_page_url, args)
                # 已经爬取数统计
                already_crawler_count += 1
                self.sinOut.emit(
                    '{cur_page} / {total_pages}页 数量：{count} ID：{id}'.format(cur_page=cur_page,
                                                                            total_pages=total_pages,
                                                                            count=already_crawler_count,
                                                                            id=fieldset_id
                                                                            ))
            if next_page > self.crawl_maximum:
                # 判断是否已经到达爬取次数
                self.sinOut.emit("已到爬取的请求数量 %s 【结束】" % str(self.crawl_maximum))
                break
            gopage = 'goPage({page},this)'.format(page=next_page)
            self.driver.execute_script(gopage)
            # 滚动页面
            self.driver.execute_script('window.scrollBy(0, 2000)')

    def add_chapter_to_db(self, fieldset_id, detail_page_url, args):
        item_bank_init = dict()
        item_bank_init['fieldset_id'] = fieldset_id
        item_bank_init['detail_page_url'] = detail_page_url
        item_bank_init['ques_url'] = args.get('url')
        item_bank_init['from_code'] = self.from_code
        item_bank_init['item_style_code'] = args.get('item_style_code')
        item_bank_init['library_id'] = args.get('library_id')
        item_bank_init['chaper_id'] = self.chapter_id
        item_bank_init['is_finish'] = 0
        mutex.acquire()
        self.db_connect.add(ItemBankInit(**item_bank_init))
        mutex.release()

    def get_item_bank_init_url(self, chapter_id, subject_code):
        """
        获取题库url列表用来爬取数据
        :return:
        """
        re_dict = dict()
        query = self.db_session.query(LibraryChapter).filter(LibraryChapter.id == chapter_id)
        url_str = 'http://www.jyeoo.com/{subject}/ques/search?f=0&q={pk}&so={from_code}'
        last_data = None
        # 遍历章节
        for item in query:
            if last_data:
                is_ok_count = self.db_session.query(ItemBankInit).filter(ItemBankInit.chaper_id == last_data.id).count()
                if is_ok_count > 1:
                    last_data.is_finish = 1
                    mutex.acquire()
                    self.db_session.commit()
                    mutex.release()
            last_data = item
            temp_dict = dict()
            # 学科
            temp_dict['subject'] = subject_code
            # 教材ID
            temp_dict['library_id'] = item.library_id
            # 章节ID
            temp_dict['chaper_id'] = item.id
            # 章节直连
            temp_dict['pk'] = item.pk
            # 题型
            temp_dict['item_style_code'] = ''
            # 题类
            temp_dict['field_code'] = ''
            # 来源
            temp_dict['from_code'] = self.from_code
            temp_dict['url'] = url_str.format(**temp_dict)
            re_dict[item.id] = temp_dict
            yield re_dict

    def get_chapter_url(self):
        url_str = 'http://www.jyeoo.com/{subject}/ques/search?f=0&q={id}'
        re_url = url_str.format(subject=self.subject_code, id=self.teaching)
        return re_url

    def get_details_url(self):
        """
        获取详情页url
        :return: list
        """

        item_bank_init = self.db_session.query(ItemBankInit).filter(ItemBankInit.chaper_id == self.chapter_id)
        for item in item_bank_init:
            re_dict = dict(
                detail_page_url=item.detail_page_url,
                from_code=item.from_code,
                chaper_id=item.chaper_id,
                item_style_code=item.item_style_code,
                library_id=item.library_id,
                fieldset_id=item.fieldset_id
            )
            yield re_dict
