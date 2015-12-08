# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'portlist.ui'
#
# Created: Tue Dec 08 14:28:27 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class PortPage(QtGui.QWidget):
    def __init__(self,parent=None):
        super(PortPage,self).__init__(parent)

        # 变量定义
        self.port_list_now_page   = 1
        self.port_list_tot_page   = 1

        # 创建标签页
        self.port_tabWidget = QtGui.QTabWidget()
        self.port_tabWidget.setObjectName(_fromUtf8("port_tabWidget"))

        # 添加端口列表页
        self.addPortListTab()

        # 添加端口管理页
        self.addPortManageTab()

    def addPortListTab(self):
        # 第一个标签页
        self.port_list_tab = QtGui.QWidget()
        self.port_list_tab.setObjectName(_fromUtf8("端口列表"))

        # logo
        self.port_list_logo_widget = QtGui.QWidget(self.port_list_tab)
        self.port_list_logo_widget.setGeometry(QtCore.QRect(28, 6, 200, 31))
        self.port_list_logo_widget.setObjectName(_fromUtf8("port_list_logo_widget"))
        self.port_list_logo_widget.setStyleSheet(_fromUtf8("border-image: url(:/image/port_list.png);"))

        # 端口列表框
        self.port_list_tableWidget = QtGui.QTableWidget(self.port_list_tab)
        self.port_list_tableWidget.setGeometry(QtCore.QRect(5, 41, 625, 271))
        self.port_list_tableWidget.setObjectName(_fromUtf8("port_list_tableWidget"))

        self.port_list_tableWidget.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.port_list_tableWidget.verticalHeader().setVisible(False)
        self.port_list_tableWidget.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.port_list_tableWidget.setAlternatingRowColors(True)
        self.port_list_tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.port_list_tableWidget.setRowCount(10)
        self.port_list_tableWidget.setColumnCount(7)
        self.port_list_tableWidget.setHorizontalHeaderLabels([_fromUtf8("PID"),_fromUtf8("协议"),_fromUtf8("本地IP"),_fromUtf8("本地端口"),_fromUtf8("外部IP"),_fromUtf8("外部端口"),_fromUtf8("进程")])
        self.port_list_tableWidget.setShowGrid(False)
        #self.port_list_tableWidget.setColumnWidth(0,568)
        self.port_list_tableWidget.setColumnWidth(0,60)
        self.port_list_tableWidget.setColumnWidth(1,60)
        self.port_list_tableWidget.setColumnWidth(2,90)
        self.port_list_tableWidget.setColumnWidth(3,60)
        self.port_list_tableWidget.setColumnWidth(4,90)
        self.port_list_tableWidget.setColumnWidth(5,60)
        self.port_list_tableWidget.setColumnWidth(6,200)
        
        # 循环添加
        for i in range(0, 10):
            self.port_list_tableWidget.setRowHeight(i,21)

        # 首页
        self.port_list_first_btn = QtGui.QPushButton(self.port_list_tab)
        self.port_list_first_btn.setGeometry(QtCore.QRect(10, 318, 75, 23))
        self.port_list_first_btn.setObjectName(_fromUtf8("port_list_first_btn"))
        self.port_list_first_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.port_list_first_btn.setText(_translate("Form", "首页", None))

        # 上一页
        self.port_list_prev_btn = QtGui.QPushButton(self.port_list_tab)
        self.port_list_prev_btn.setGeometry(QtCore.QRect(90, 318, 75, 23))
        self.port_list_prev_btn.setObjectName(_fromUtf8("port_list_prev_btn"))
        self.port_list_prev_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.port_list_prev_btn.setText(_translate("Form", "上一页", None))

        # 下一页
        self.port_list_next_btn = QtGui.QPushButton(self.port_list_tab)
        self.port_list_next_btn.setGeometry(QtCore.QRect(230, 318, 75, 23))
        self.port_list_next_btn.setObjectName(_fromUtf8("port_list_next_btn"))
        self.port_list_next_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.port_list_next_btn.setText(_translate("Form", "下一页", None))

        # 确定按钮
        self.port_list_ok_btn = QtGui.QPushButton(self.port_list_tab)
        self.port_list_ok_btn.setGeometry(QtCore.QRect(540, 318, 75, 23))
        self.port_list_ok_btn.setObjectName(_fromUtf8("port_list_ok_btn"))
        self.port_list_ok_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.port_list_ok_btn.setText(_translate("Form", "确定", None))
        
        #当前页标签        
        self.port_list_now_label = QtGui.QLabel(self.port_list_tab)
        self.port_list_now_label.setGeometry(QtCore.QRect(172, 318, 50, 23))
        self.port_list_now_label.setAlignment(QtCore.Qt.AlignCenter)
        self.port_list_now_label.setObjectName(_fromUtf8("port_list_now_label"))
        self.port_list_now_label.setText(_translate("Form", "0", None))

        # 总页数标签
        self.port_list_tot_label = QtGui.QLabel(self.port_list_tab)
        self.port_list_tot_label.setGeometry(QtCore.QRect(340, 318, 54, 23))
        self.port_list_tot_label.setObjectName(_fromUtf8("port_list_tot_label"))
        self.port_list_tot_label.setText(_translate("Form", "共1页", None))

        # 标签跳转
        self.label_3 = QtGui.QLabel(self.port_list_tab)
        self.label_3.setGeometry(QtCore.QRect(420, 318, 32, 23))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setText(_translate("Form", "跳到", None))

        # 跳转输入框
        self.port_list_jump_edit = QtGui.QLineEdit(self.port_list_tab)
        self.port_list_jump_edit.setGeometry(QtCore.QRect(460, 318, 70, 23))
        self.port_list_jump_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.port_list_jump_edit.setObjectName(_fromUtf8("port_list_jump_edit"))
        self.port_list_jump_edit.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.port_list_jump_edit.setText(_translate("Form", "0", None))
        
        # 查询按钮
        self.port_list_query_btn = QtGui.QPushButton(self.port_list_tab)
        self.port_list_query_btn.setGeometry(QtCore.QRect(565, 10, 60, 23))
        self.port_list_query_btn.setObjectName(_fromUtf8("port_list_query_btn"))
        self.port_list_query_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.port_list_query_btn.setText(_translate("Form", "查询", None))

        # 当前页添加到标签中
        self.port_tabWidget.addTab(self.port_list_tab, _fromUtf8("端口列表"))
        
    def addPortManageTab(self): 
        self.port_manage_tab = QtGui.QWidget()
        self.port_manage_tab.setObjectName(_fromUtf8("端口管理"))
        self.port_tabWidget.addTab(self.port_manage_tab, _fromUtf8("端口管理"))


import image_rc
