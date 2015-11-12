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
    

class GuiDevice(QtGui.QWidget):
    def __init__(self,parent=None):  
        super(GuiDevice,self).__init__(parent)        
        self.setupUi(self)
        
    def AddListLeftDevice(self):
        self.device_wdg = QtGui.QWidget(self.frame_mid_right)        
        self.device_wdg.setObjectName(u"device_wdg")
        self.device_wdg.setGeometry(QtCore.QRect(18, 15, 651, 379))

        self.frame_mid_right.addWidget(self.device_wdg)

        # logo
        logo_widget = QtGui.QWidget(self.device_wdg)
        logo_widget.setGeometry(QtCore.QRect(20, 10, 200, 55))
        logo_widget.setObjectName(_fromUtf8("device_logo_widget"))
        logo_widget.setStyleSheet(_fromUtf8("border-image: url(:/image/device_logo.png);"))
        
        # push button
        ok_push_btn = QtGui.QPushButton(self.device_wdg)
        ok_push_btn.setGeometry(QtCore.QRect(520, 53, 90, 23))
        ok_push_btn.setObjectName(_fromUtf8("device_ok_push_btn"))  
        ok_push_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        ok_push_btn.setText(_translate("Form", "应用到服务器", None))

        # list widget
        self.device_row_Count = 2
        list_widget = QtGui.QTableWidget(self.device_wdg)
        list_widget.setGeometry(QtCore.QRect(20, 80, 600, 260))
        list_widget.setObjectName(_fromUtf8("device_list_widget"))
        list_widget.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        list_widget.verticalHeader().setVisible(False)
        list_widget.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        list_widget.setAlternatingRowColors(True)
        #list_widget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        list_widget.setRowCount(self.device_row_Count)
        list_widget.setColumnCount(3)
        list_widget.setHorizontalHeaderLabels([_fromUtf8("功能"),_fromUtf8("操作"),_fromUtf8("状态")])
        list_widget.setShowGrid(False)
        list_widget.setColumnWidth(0,230)
        list_widget.setColumnWidth(1,190)
        list_widget.setColumnWidth(2,160)
        for i in range(0, self.device_row_Count):
            list_widget.setRowHeight(i,40)
        self.list_widget = list_widget

        # 第一行 CDROM
        self.DeviceAddCdrom(0)
        # 第二行 USB
        self.DeviceAddUsb(1)        
        
        self.list_widget_cdrom_value = 0
        self.list_widget_usb_value = 0

        
        # 从服务器获取最新状态
        self.DeviceSetStatus()
        
        self.connect(self.list_widget, QtCore.SIGNAL("cellClicked(int,int)"), self.DeviceOnOffClick)
        self.connect(ok_push_btn, QtCore.SIGNAL("clicked()"), self.DeviceOkBtnClick)

    def DeviceAddUsb(self, line):
        # 2行 1列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 200, 40))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(30, 0, 40, 40))
        img.setAlignment(QtCore.Qt.AlignRight)
        img.setStyleSheet(_fromUtf8("image: url(:/image/device_usb.png);"))
        text = QtGui.QLabel(item)
        text.setGeometry(QtCore.QRect(90, 0, 110, 40))
        text.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        text.setText(_fromUtf8("禁用USB存储设备"))
        self.list_widget.setCellWidget(line, 0, item)
        
        # 2行 2列
        item = QtGui.QTableWidgetItem(_fromUtf8("已应用到服务器"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_widget.setItem(line, 1, item)
        self.list_widget_usb_text = item
        
        # 2行 3列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 160, 40))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(40, 5, 80, 30))
        img.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        img.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_off.png);"))
        self.list_widget.setCellWidget(line, 2, item)
        self.list_widget_usb_onoff = img
        
    def DeviceAddCdrom(self, line):
        # 1行 1列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 200, 40))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(30, 0, 40, 40))
        img.setAlignment(QtCore.Qt.AlignRight)
        img.setStyleSheet(_fromUtf8("image: url(:/image/device_cdrom.png);"))
        text = QtGui.QLabel(item)
        text.setGeometry(QtCore.QRect(90, 0, 110, 40))
        text.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        text.setText(_fromUtf8("禁用光驱"))
        self.list_widget.setCellWidget(line, 0, item)

        # 1行 2列
        item = QtGui.QTableWidgetItem(_fromUtf8("已应用到服务器"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_widget.setItem(line, 1, item)
        self.list_widget_cdrom_text = item
            
        # 1行 3列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 160, 40))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(40, 5, 80, 30))
        img.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        img.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_off.png);"))
        self.list_widget.setCellWidget(line, 2, item)
        self.list_widget_cdrom_onoff = img
    
    def DeviceOnOffClick(self, line, col):
        if line == 0 and col == 2:
            if self.list_widget_cdrom_value == 0:
                self.list_widget_cdrom_value = 1
                self.list_widget_cdrom_text.setText(_fromUtf8("等待应用到服务器"))
                self.list_widget_cdrom_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_on.png);"))
            else:
                self.list_widget_cdrom_value = 0
                self.list_widget_cdrom_text.setText(_fromUtf8("等待应用到服务器"))
                self.list_widget_cdrom_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_off.png);"))
            
        if line == 1 and col == 2:
            if self.list_widget_usb_value == 0:
                self.list_widget_usb_value = 1
                self.list_widget_usb_text.setText(_fromUtf8("等待应用到服务器"))
                self.list_widget_usb_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_on.png);"))
            else:
                self.list_widget_usb_value = 0
                self.list_widget_usb_text.setText(_fromUtf8("等待应用到服务器"))
                self.list_widget_usb_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_off.png);"))
            
    
    def DeviceOkBtnClick(self):
        url = "http://127.0.0.1:8080/config/setdevice"
        param = {'CdromStatus' :  self.list_widget_cdrom_value,
                 'UsbStatus'   : self.list_widget_usb_value
                 }
        ret = http.Post(url, param)
        if ret['ErrStat'] == 0:
            # 更新数据
            self.list_widget_cdrom_text.setText(_fromUtf8("已应用到服务器"))
            self.list_widget_usb_text.setText(_fromUtf8("已应用到服务器"))
            #QtGui.QMessageBox.about(self, u"设置", u"设置:" + "white=%d" % (chkw) + "  black=%d" % (chkb))
        else:
            QtGui.QMessageBox.about(self, u"设置", u"设置失败:" + ret['ErrMsg'])

    def DeviceSetStatus(self):
        url = "http://127.0.0.1:8080/config/getdevice"
        param = {}
        ret = http.Post(url, param)
        if ret['ErrStat'] == 0:
            # 更新数据
            self.list_widget_cdrom_value = ret['Config']['CdromStatus']
            self.list_widget_usb_value   = ret['Config']['UsbStatus']
            if self.list_widget_cdrom_value == 1:
                self.list_widget_cdrom_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_on.png);"))
            else:
                self.list_widget_cdrom_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_off.png);"))

            if self.list_widget_usb_value == 1:
                self.list_widget_usb_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_on.png);"))
            else:
                self.list_widget_usb_onoff.setStyleSheet(_fromUtf8("border-image: url(:/image/btn_off.png);"))
            #QtGui.QMessageBox.about(self, u"设置", u"设置:" + "white=%d" % (chkw) + "  black=%d" % (chkb))
        else:
            QtGui.QMessageBox.about(self, u"设置", u"设置失败:" + ret['ErrMsg'])
        
