# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 1084)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 961, 131))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_account = QtWidgets.QLabel(self.groupBox)
        self.label_account.setObjectName("label_account")
        self.horizontalLayout.addWidget(self.label_account)
        self.label_account_content = QtWidgets.QLabel(self.groupBox)
        self.label_account_content.setObjectName("label_account_content")
        self.horizontalLayout.addWidget(self.label_account_content)
        self.pushButton_change = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_change.setObjectName("pushButton_change")
        self.horizontalLayout.addWidget(self.pushButton_change)
        self.pushButton_getAccount = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_getAccount.setObjectName("pushButton_getAccount")
        self.horizontalLayout.addWidget(self.pushButton_getAccount)
        spacerItem = QtWidgets.QSpacerItem(480, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_logout = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_logout.setEnabled(False)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.horizontalLayout.addWidget(self.pushButton_logout)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 160, 981, 521))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 941, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.comboBox_grade = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_grade.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.comboBox_grade.setObjectName("comboBox_grade")
        self.gridLayout.addWidget(self.comboBox_grade, 0, 3, 1, 1)
        self.comboBox_teaching = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_teaching.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.comboBox_teaching.setObjectName("comboBox_teaching")
        self.gridLayout.addWidget(self.comboBox_teaching, 1, 3, 1, 1)
        self.comboBox_subject = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_subject.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.comboBox_subject.setObjectName("comboBox_subject")
        self.gridLayout.addWidget(self.comboBox_subject, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 2, 1, 1)
        self.pushButton_loaddata = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_loaddata.setObjectName("pushButton_loaddata")
        self.gridLayout.addWidget(self.pushButton_loaddata, 0, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 2, 1, 1)
        self.comboBox_level = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_level.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBox_level.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.comboBox_level.setObjectName("comboBox_level")
        self.gridLayout.addWidget(self.comboBox_level, 0, 1, 1, 1)
        self.comboBox_chapter = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_chapter.setEnabled(False)
        self.comboBox_chapter.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.comboBox_chapter.setEditable(False)
        self.comboBox_chapter.setObjectName("comboBox_chapter")
        self.gridLayout.addWidget(self.comboBox_chapter, 2, 1, 1, 1)
        self.lcdNumber_chapter = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_chapter.setDigitCount(6)
        self.lcdNumber_chapter.setObjectName("lcdNumber_chapter")
        self.gridLayout.addWidget(self.lcdNumber_chapter, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.treeWidget_chapter = QtWidgets.QTreeWidget(self.layoutWidget)
        self.treeWidget_chapter.setHeaderHidden(True)
        self.treeWidget_chapter.setColumnCount(1)
        self.treeWidget_chapter.setObjectName("treeWidget_chapter")
        self.treeWidget_chapter.headerItem().setText(0, "1")
        self.treeWidget_chapter.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeWidget_chapter)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 710, 981, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 891, 139))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_restart = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_restart.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButton_restart.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.radioButton_restart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_restart.setAutoFillBackground(False)
        self.radioButton_restart.setCheckable(True)
        self.radioButton_restart.setChecked(True)
        self.radioButton_restart.setAutoRepeat(False)
        self.radioButton_restart.setObjectName("radioButton_restart")
        self.horizontalLayout_5.addWidget(self.radioButton_restart)
        self.radioButton_continue = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_continue.setEnabled(False)
        self.radioButton_continue.setCheckable(False)
        self.radioButton_continue.setChecked(False)
        self.radioButton_continue.setObjectName("radioButton_continue")
        self.horizontalLayout_5.addWidget(self.radioButton_continue)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 1, 0, 1, 1)
        self.spinBox_crawlMaximum = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_crawlMaximum.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.spinBox_crawlMaximum.setMinimum(1)
        self.spinBox_crawlMaximum.setMaximum(5000)
        self.spinBox_crawlMaximum.setProperty("value", 100)
        self.spinBox_crawlMaximum.setObjectName("spinBox_crawlMaximum")
        self.gridLayout_2.addWidget(self.spinBox_crawlMaximum, 1, 1, 1, 1)
        self.progressBar_crawler = QtWidgets.QProgressBar(self.layoutWidget1)
        self.progressBar_crawler.setMaximumSize(QtCore.QSize(500, 16777215))
        self.progressBar_crawler.setProperty("value", 0)
        self.progressBar_crawler.setObjectName("progressBar_crawler")
        self.gridLayout_2.addWidget(self.progressBar_crawler, 1, 2, 1, 1)
        self.label_from = QtWidgets.QLabel(self.layoutWidget1)
        self.label_from.setObjectName("label_from")
        self.gridLayout_2.addWidget(self.label_from, 0, 0, 1, 1)
        self.comboBox_from = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_from.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.comboBox_from.setObjectName("comboBox_from")
        self.gridLayout_2.addWidget(self.comboBox_from, 0, 1, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_2.addWidget(self.pushButton_start, 1, 3, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        self.label_5.setObjectName("label_5")
        self.lcdNumber_from = QtWidgets.QLCDNumber(self.splitter)
        self.lcdNumber_from.setDigitCount(6)
        self.lcdNumber_from.setObjectName("lcdNumber_from")
        self.gridLayout_2.addWidget(self.splitter, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 60, 891, 53))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.spinBox_details = QtWidgets.QSpinBox(self.layoutWidget2)
        self.spinBox_details.setMaximum(1000)
        self.spinBox_details.setProperty("value", 100)
        self.spinBox_details.setObjectName("spinBox_details")
        self.horizontalLayout_4.addWidget(self.spinBox_details)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.progressBar_details = QtWidgets.QProgressBar(self.layoutWidget2)
        self.progressBar_details.setProperty("value", 0)
        self.progressBar_details.setObjectName("progressBar_details")
        self.horizontalLayout_4.addWidget(self.progressBar_details)
        self.pushButton_start_details = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_start_details.setEnabled(True)
        self.pushButton_start_details.setCheckable(False)
        self.pushButton_start_details.setAutoDefault(False)
        self.pushButton_start_details.setObjectName("pushButton_start_details")
        self.horizontalLayout_4.addWidget(self.pushButton_start_details)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(40, 30, 861, 101))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.progressBar_crawler_chapter = QtWidgets.QProgressBar(self.layoutWidget3)
        self.progressBar_crawler_chapter.setMaximumSize(QtCore.QSize(500, 16777215))
        self.progressBar_crawler_chapter.setProperty("value", 0)
        self.progressBar_crawler_chapter.setObjectName("progressBar_crawler_chapter")
        self.gridLayout_5.addWidget(self.progressBar_crawler_chapter, 0, 0, 1, 1)
        self.pushButton_start_chapter = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_start_chapter.setObjectName("pushButton_start_chapter")
        self.gridLayout_5.addWidget(self.pushButton_start_chapter, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 41))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setAccessibleName("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDB = QtWidgets.QAction(MainWindow)
        self.actionDB.setObjectName("actionDB")
        self.actionUpgrade = QtWidgets.QAction(MainWindow)
        self.actionUpgrade.setEnabled(False)
        self.actionUpgrade.setObjectName("actionUpgrade")
        self.menu.addAction(self.actionDB)
        self.menu.addAction(self.actionUpgrade)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_change, self.pushButton_getAccount)
        MainWindow.setTabOrder(self.pushButton_getAccount, self.pushButton_logout)
        MainWindow.setTabOrder(self.pushButton_logout, self.comboBox_level)
        MainWindow.setTabOrder(self.comboBox_level, self.spinBox_crawlMaximum)
        MainWindow.setTabOrder(self.spinBox_crawlMaximum, self.pushButton_start)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "账号信息"))
        self.label_account.setText(_translate("MainWindow", "账号："))
        self.label_account_content.setText(_translate("MainWindow", "未知"))
        self.pushButton_change.setText(_translate("MainWindow", "切换"))
        self.pushButton_getAccount.setText(_translate("MainWindow", "获取账号"))
        self.pushButton_logout.setText(_translate("MainWindow", "注销"))
        self.groupBox_3.setTitle(_translate("MainWindow", "筛选条件"))
        self.label_10.setText(_translate("MainWindow", "学级"))
        self.label_3.setText(_translate("MainWindow", "已有："))
        self.label_11.setText(_translate("MainWindow", "学科"))
        self.label_20.setText(_translate("MainWindow", "教材"))
        self.pushButton_loaddata.setText(_translate("MainWindow", "加载数据"))
        self.label_18.setText(_translate("MainWindow", "章节"))
        self.label_12.setText(_translate("MainWindow", "年级"))
        self.groupBox_2.setTitle(_translate("MainWindow", "操作分类"))
        self.radioButton_restart.setText(_translate("MainWindow", "重新开始"))
        self.radioButton_continue.setText(_translate("MainWindow", "断点续爬"))
        self.label_19.setText(_translate("MainWindow", "次数"))
        self.label_from.setText(_translate("MainWindow", "来源"))
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.label_5.setText(_translate("MainWindow", "已有："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "题库"))
        self.label_2.setText(_translate("MainWindow", "数量："))
        self.label_4.setText(_translate("MainWindow", "进度："))
        self.pushButton_start_details.setText(_translate("MainWindow", "开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "详情页"))
        self.pushButton_start_chapter.setText(_translate("MainWindow", "开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "章节"))
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.actionDB.setText(_translate("MainWindow", "数据库"))
        self.actionUpgrade.setText(_translate("MainWindow", "检查更新"))


