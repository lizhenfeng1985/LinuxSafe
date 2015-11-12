# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys  
import main
import http
import config

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
    

class GuiSpecrc(QtGui.QWidget):
    def __init__(self,parent=None):  
        super(GuiSpecrc,self).__init__(parent)        
        self.setupUi(self)
        
    def AddListLeftSpecrc(self):
        self.specrc_wdg = QtGui.QWidget(self.frame_mid_right)        
        self.specrc_wdg.setObjectName(u"specrc_wdg")
        self.specrc_wdg.setGeometry(QtCore.QRect(18, 15, 651, 379))

        self.frame_mid_right.addWidget(self.specrc_wdg)

        # logo
        logo_widget = QtGui.QWidget(self.specrc_wdg)
        logo_widget.setGeometry(QtCore.QRect(20, 10, 200, 55))
        logo_widget.setObjectName(_fromUtf8("specrc_logo_widget"))
        logo_widget.setStyleSheet(_fromUtf8("border-image: url(:/image/specrc_logo.png);"))
        
        # push button
        ok_push_btn = QtGui.QPushButton(self.specrc_wdg)
        ok_push_btn.setGeometry(QtCore.QRect(520, 53, 90, 23))
        ok_push_btn.setObjectName(_fromUtf8("specrc_ok_push_btn"))  
        ok_push_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        ok_push_btn.setText(_translate("Form", "应用到服务器", None))

        # list widget
        self.specrc_row_Count = 2
        list_widget = QtGui.QTableWidget(self.specrc_wdg)
        list_widget.setGeometry(QtCore.QRect(20, 80, 600, 260))
        list_widget.setObjectName(_fromUtf8("specrc_list_widget"))
        list_widget.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        list_widget.verticalHeader().setVisible(False)
        list_widget.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        list_widget.setAlternatingRowColors(True)
        #list_widget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        list_widget.setRowCount(self.specrc_row_Count)
        list_widget.setColumnCount(3)
        list_widget.setHorizontalHeaderLabels([_fromUtf8("功能"),_fromUtf8("操作"),_fromUtf8("状态")])
        list_widget.setShowGrid(False)
        list_widget.setColumnWidth(0,230)
        list_widget.setColumnWidth(1,190)
        list_widget.setColumnWidth(2,160)
        for i in range(0, self.specrc_row_Count):
            list_widget.setRowHeight(i,40)
        self.list_widget = list_widget

        # 第一行 禁止修改时间
        self.AddSetTime(0)
        
        # 第二行 禁止关机
        self.SpecrcAddShutDown(1) 
        
        self.list_widget_shutdown_value = 0
        self.list_widget_settime_value  = 0

        
        # 从服务器获取最新状态
        self.SpecrcSetStatus()
        
        self.connect(self.list_widget, QtCore.SIGNAL("cellClicked(int,int)"), self.SpecrcOnOffClick)
        self.connect(ok_push_btn, QtCore.SIGNAL("clicked()"), self.SpecrcOkBtnClick)

    def AddSetTime(self, line):
        # 2行 1列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 200, 40))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(30, 0, 35, 35))
        img.setAlignment(QtCore.Qt.AlignRight)
        img.setStyleSheet(_fromUtf8("image: url(:/image/specrc_settime.png);"))
        text = QtGui.QLabel(item)
        text.setGeometry(QtCore.QRect(90, 0, 110, 40))
        text.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        text.setText(_fromUtf8("禁止修改系统时间"))
        self.list_widget.setCellWidget(line, 0, item)
        
        # 2行 2列
        item = QtGui.QTableWidgetItem(_fromUtf8("已应用到服务器"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_widget.setItem(line, 1, item)
        self.list_widget_settime_text = item
        
        # 2行 3列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 160, 40))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(40, 5, 80, 30))
        img.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        img.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_off.png);"))
        self.list_widget.setCellWidget(line, 2, item)
        self.list_widget_settime_onoff = img
        
    def SpecrcAddShutDown(self, line):
        # 1行 1列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 200, 40))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(30, 0, 35, 35))
        img.setAlignment(QtCore.Qt.AlignRight)
        img.setStyleSheet(_fromUtf8("image: url(:/image/specrc_shutdown.png);"))
        text = QtGui.QLabel(item)
        text.setGeometry(QtCore.QRect(90, 0, 110, 40))
        text.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        text.setText(_fromUtf8("禁止关机和重启"))
        self.list_widget.setCellWidget(line, 0, item)

        # 1行 2列
        item = QtGui.QTableWidgetItem(_fromUtf8("已应用到服务器"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_widget.setItem(line, 1, item)
        self.list_widget_shutdown_text = item
            
        # 1行 3列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 160, 40))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(40, 5, 80, 30))
        img.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        img.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_off.png);"))
        self.list_widget.setCellWidget(line, 2, item)
        self.list_widget_shutdown_onoff = img
    
    def SpecrcOnOffClick(self, line, col):        
        if line == 0 and col == 2:
            if self.list_widget_settime_value == 0:
                self.list_widget_settime_value = 1
                self.list_widget_settime_text.setText(_fromUtf8("等待应用到服务器"))
                self.list_widget_settime_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_on.png);"))
            else:
                self.list_widget_settime_value = 0
                self.list_widget_settime_text.setText(_fromUtf8("等待应用到服务器"))
                self.list_widget_settime_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_off.png);"))
                
        if line == 1 and col == 2:
            if self.list_widget_shutdown_value == 0:
                self.list_widget_shutdown_value = 1
                self.list_widget_shutdown_text.setText(_fromUtf8("等待应用到服务器"))
                self.list_widget_shutdown_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_on.png);"))
            else:
                self.list_widget_shutdown_value = 0
                self.list_widget_shutdown_text.setText(_fromUtf8("等待应用到服务器"))
                self.list_widget_shutdown_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_off.png);"))

            
    def SpecrcOkBtnClick(self):
        url = "http://127.0.0.1:8080/config/setspecrc"
        param = {'ShutDownStatus' :  self.list_widget_shutdown_value,
                 'SetTimeStatus'   : self.list_widget_settime_value
                 }
        ret = http.Post(url, param)
        if ret['ErrStat'] == 0:
            # 更新数据
            self.list_widget_shutdown_text.setText(_fromUtf8("已应用到服务器"))
            self.list_widget_settime_text.setText(_fromUtf8("已应用到服务器"))
        else:
            QtGui.QMessageBox.about(self, u"设置", u"设置失败:" + ret['ErrMsg'])

    def SpecrcSetStatus(self):
        url = "http://127.0.0.1:8080/config/getspecrc"
        param = {}
        ret = http.Post(url, param)
        if ret['ErrStat'] == 0:
            # 更新数据
            self.list_widget_shutdown_value = ret['Config']['ShutDownStatus']
            self.list_widget_settime_value   = ret['Config']['SetTimeStatus']
            if self.list_widget_shutdown_value == 1:
                self.list_widget_shutdown_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_on.png);"))
            else:
                self.list_widget_shutdown_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_off.png);"))

            if self.list_widget_settime_value == 1:
                self.list_widget_settime_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_on.png);"))
            else:
                self.list_widget_settime_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_off.png);"))
        else:
            QtGui.QMessageBox.about(self, u"设置", u"设置失败:" + ret['ErrMsg'])
        
