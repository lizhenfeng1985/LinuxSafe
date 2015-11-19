# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created: Thu Nov 19 20:32:39 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class LogPage(QtGui.QWidget):
    def __init__(self,parent=None):
        super(LogPage,self).__init__(parent)

        # 变量定义
        t = time.localtime()
        self.log_url_start_time = "%04d-%2d-%02d 00:00:00" % (t.tm_year, t.tm_mon, t.tm_mday)
        self.log_url_stop_time  = "%04d-%2d-%02d 23:59:59" % (t.tm_year, t.tm_mon, t.tm_mday)
        self.log_url_quert_word = ""
        self.log_url_now_page   = 1
        self.log_url_tot_page   = 1     
        
        # 创建标签页
        self.log_tabWidget = QtGui.QTabWidget()
        self.log_tabWidget.setObjectName(_fromUtf8("log_tabWidget"))

        # 添加日志页
        self.addUrlLogTab()

        # 添加外设页
        self.addDeviceLogTab()

        # 添加特殊资源页
        self.addSpecrcLogTab()

    def addUrlLogTab(self):
        # 第一个标签页
        self.url_tab = QtGui.QWidget()
        self.url_tab.setObjectName(_fromUtf8("URL"))

        # 日志列表框
        self.url_log_tableWidget = QtGui.QTableWidget(self.url_tab)
        self.url_log_tableWidget.setGeometry(QtCore.QRect(5, 41, 625, 271))
        self.url_log_tableWidget.setObjectName(_fromUtf8("url_log_tableWidget"))

        self.url_log_tableWidget.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.url_log_tableWidget.verticalHeader().setVisible(False)
        self.url_log_tableWidget.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.url_log_tableWidget.setAlternatingRowColors(True)
        self.url_log_tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.url_log_tableWidget.setRowCount(10)
        self.url_log_tableWidget.setColumnCount(8)
        self.url_log_tableWidget.setHorizontalHeaderLabels([_fromUtf8("类型"),_fromUtf8("PID"),_fromUtf8("用户"),_fromUtf8("进程"),_fromUtf8("IP端口"),_fromUtf8("URL"),_fromUtf8("结果"),_fromUtf8("时间")])
        self.url_log_tableWidget.setShowGrid(False)
        #self.url_log_tableWidget.setColumnWidth(0,568)
        self.url_log_tableWidget.setColumnWidth(0,70)
        self.url_log_tableWidget.setColumnWidth(1,70)
        self.url_log_tableWidget.setColumnWidth(2,70)
        self.url_log_tableWidget.setColumnWidth(3,70)
        self.url_log_tableWidget.setColumnWidth(4,70)
        self.url_log_tableWidget.setColumnWidth(5,70)
        self.url_log_tableWidget.setColumnWidth(6,70)
        self.url_log_tableWidget.setColumnWidth(7,70)
        
        # 循环添加
        for i in range(0, 10):
            self.url_log_tableWidget.setRowHeight(i,21)

        # 日志 - 首页
        self.log_url_first_btn = QtGui.QPushButton(self.url_tab)
        self.log_url_first_btn.setGeometry(QtCore.QRect(10, 315, 75, 23))
        self.log_url_first_btn.setObjectName(_fromUtf8("log_url_first_btn"))
        self.log_url_first_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.log_url_first_btn.setText(_fromUtf8("首页"))
        
        # 日志 - 上一页
        self.log_url_prev_btn = QtGui.QPushButton(self.url_tab)
        self.log_url_prev_btn.setGeometry(QtCore.QRect(90, 315, 75, 23))
        self.log_url_prev_btn.setObjectName(_fromUtf8("log_url_prev_btn"))
        self.log_url_prev_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.log_url_prev_btn.setText(_fromUtf8("上一页"))
                
        # 日志 - 下一页
        self.log_url_next_btn = QtGui.QPushButton(self.url_tab)
        self.log_url_next_btn.setGeometry(QtCore.QRect(230, 315, 75, 23))
        self.log_url_next_btn.setObjectName(_fromUtf8("log_url_next_btn"))
        self.log_url_next_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.log_url_next_btn.setText(_fromUtf8("下一页"))
        
        # 日志 - 确定跳转
        self.log_url_ok_btn = QtGui.QPushButton(self.url_tab)
        self.log_url_ok_btn.setGeometry(QtCore.QRect(540, 315, 75, 23))
        self.log_url_ok_btn.setObjectName(_fromUtf8("log_url_ok_btn"))
        self.log_url_ok_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.log_url_ok_btn.setText(_fromUtf8("确定"))

        # 日志 - 当前页码
        self.log_url_now_label = QtGui.QLabel(self.url_tab)
        self.log_url_now_label.setGeometry(QtCore.QRect(172, 315, 50, 23))
        self.log_url_now_label.setAlignment(QtCore.Qt.AlignCenter)
        self.log_url_now_label.setObjectName(_fromUtf8("log_url_now_label"))
        self.log_url_now_label.setText(_fromUtf8("0"))
        
        # 日志 - 总页码        
        self.log_url_tot_label = QtGui.QLabel(self.url_tab)
        self.log_url_tot_label.setGeometry(QtCore.QRect(340, 315, 54, 23))
        self.log_url_tot_label.setObjectName(_fromUtf8("log_url_tot_label"))        
        self.log_url_tot_label.setText(_fromUtf8("共1页"))
        self.log_url_tot_label.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        
        # 日志 - 文字 - 跳到
        self.label_3 = QtGui.QLabel(self.url_tab)
        self.label_3.setGeometry(QtCore.QRect(420, 315, 32, 23))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setText(_fromUtf8("跳到"))        

        # 日志 - 跳转- 输入页码框
        self.log_url_jump_edit = QtGui.QLineEdit(self.url_tab)
        self.log_url_jump_edit.setGeometry(QtCore.QRect(460, 315, 70, 23))
        self.log_url_jump_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.log_url_jump_edit.setObjectName(_fromUtf8("log_url_jump_edit"))
        self.log_url_jump_edit.setText(_fromUtf8("0"))
        self.log_url_jump_edit.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))

        # 日志 - 开始时间 - 文字
        self.label = QtGui.QLabel(self.url_tab)
        self.label.setGeometry(QtCore.QRect(7, 10, 50, 23))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setText(_fromUtf8("开始时间"))
        self.label.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))

        # 日志 - 结束时间 - 文字
        self.label_2 = QtGui.QLabel(self.url_tab)
        self.label_2.setGeometry(QtCore.QRect(214, 10, 54, 23))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setText(_fromUtf8("结束时间"))
        self.label_2.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))

        # 日志 - 开始时间 - 时间控件
        self.log_url_start_timeedit = QtGui.QDateTimeEdit(self.url_tab)
        self.log_url_start_timeedit.setGeometry(QtCore.QRect(60, 10, 145, 23))
        self.log_url_start_timeedit.setObjectName(_fromUtf8("log_url_start_timeedit"))
        self.log_url_start_timeedit.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.log_url_start_timeedit.setDateTime(QtCore.QDateTime.fromString(self.log_url_start_time, 'yyyy-MM-dd hh:mm:ss'))

        # 日志 - 结束时间 - 时间控件
        self.log_url_stop_timeedit = QtGui.QDateTimeEdit(self.url_tab)
        self.log_url_stop_timeedit.setGeometry(QtCore.QRect(263, 10, 145, 23))
        self.log_url_stop_timeedit.setObjectName(_fromUtf8("log_url_stop_timeedit"))
        self.log_url_stop_timeedit.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.log_url_stop_timeedit.setDateTime(QtCore.QDateTime.fromString(self.log_url_stop_time, 'yyyy-MM-dd hh:mm:ss'))

        # 日志 - 模糊查询 - 输入框
        self.log_url_query_edit = QtGui.QLineEdit(self.url_tab)
        self.log_url_query_edit.setGeometry(QtCore.QRect(418, 10, 142, 23))
        self.log_url_query_edit.setObjectName(_fromUtf8("log_url_query_edit"))
        self.log_url_query_edit.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.log_url_query_edit.setText(_fromUtf8(""))
        

        # 日志 - 查询 - 按纽
        self.log_url_query_btn = QtGui.QPushButton(self.url_tab)
        self.log_url_query_btn.setGeometry(QtCore.QRect(565, 10, 60, 23))
        self.log_url_query_btn.setObjectName(_fromUtf8("log_url_query_btn"))
        self.log_url_query_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.log_url_query_btn.setText(_fromUtf8("查询"))
        
        # 添加url到标签
        self.log_tabWidget.addTab(self.url_tab, _fromUtf8("URL过滤"))

    def addDeviceLogTab(self):
        self.device_tab = QtGui.QWidget()
        self.device_tab.setObjectName(_fromUtf8("device_tab"))
        self.log_tabWidget.addTab(self.device_tab, _fromUtf8("外设管理"))

    def addSpecrcLogTab(self):
        self.specrc_tab = QtGui.QWidget()
        self.specrc_tab.setObjectName(_fromUtf8("specrc_tab"))
        self.log_tabWidget.addTab(self.specrc_tab, _fromUtf8("特殊资源"))

import image_rc
