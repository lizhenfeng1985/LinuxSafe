# -*- coding: utf-8 -*-
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys 
import ui_port
import http
import config

_encoding = QApplication.UnicodeUTF8

class GuiPort(QWidget):
    def __init__(self,parent=None):  
        super(GuiPort,self).__init__(parent)        
        self.setupUi(self)
        
    def AddListLeftPort(self):
        self.port_page = ui_port.PortPage()
        self.frame_mid_right.addWidget(self.port_page.port_tabWidget)        
        self.connect(self.listWidget_left,SIGNAL("currentRowChanged(int)"),self.frame_mid_right,SLOT("setCurrentIndex(int)"))

        # 消息处理
        self.connect(self.port_page.port_list_first_btn, SIGNAL("clicked()"), self.PortPageList_First)
        self.connect(self.port_page.port_list_prev_btn, SIGNAL("clicked()"), self.PortPageList_Prev)
        self.connect(self.port_page.port_list_next_btn, SIGNAL("clicked()"), self.PortPageList_Next)
        self.connect(self.port_page.port_list_ok_btn, SIGNAL("clicked()"), self.PortPageList_OK)
        self.connect(self.port_page.port_list_query_btn, SIGNAL("clicked()"), self.PortPageList_Query)

    def PortPageList_First(self):
        self.port_page.port_list_now_page = 1
        self.PortPageList_SetList()

    def PortPageList_Prev(self):
        if self.port_page.port_list_now_page == 1:
            QMessageBox.about(self, u"获取使用端口列表", u"错误:已经是第一页")
        else:
            self.port_page.port_list_now_page -= 1
            self.PortPageList_SetList()

    def PortPageList_Next(self):
        if self.port_page.port_list_now_page == self.port_page.port_list_tot_page:
            QMessageBox.about(self, u"获取使用端口列表", u"错误:已经是第最后一页")
        else:
            self.port_page.port_list_now_page += 1
            self.PortPageList_SetList()

    def PortPageList_OK(self):
        try:
            jmpstr = self.port_page.port_list_jump_edit.text()
            jmpint = int(jmpstr)
            if jmpint < 1 or jmpint > self.port_page.port_list_tot_page:
                QMessageBox.about(self, u"获取使用端口列表", u"错误:页码输入错误")
            else:
                self.port_page.port_list_now_page = jmpint
                self.PortPageList_SetList()
        except:
            QMessageBox.about(self, u"获取使用端口列表", u"错误:页码输入错误")

    def PortPageList_Query(self):
        self.PortPageList_SetList()

    def PortPageList_SetList(self):
        MaxLines  = 10    
        url = "%s/port/list/query" % (config.GLB_CFG['SRV_URL'])
        param = {'Start'     : (self.port_page.port_list_now_page - 1) * MaxLines,
                 'Length'    : MaxLines,
                 }
        ret = http.Post(url, param)
        
        if ret['ErrStat'] == 0:
            # 清空列表
            for i in range(0, 10):
                for j in range(0, 7):
                    self.port_page.port_list_tableWidget.setItem(i, j, None)                
                
            # 添加列表
            for i in range(0, len(ret['Lists'])):
                newItem = QTableWidgetItem(ret['Lists'][i]['Pid'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.port_page.port_list_tableWidget.setItem(i, 0, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Type'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.port_page.port_list_tableWidget.setItem(i, 1, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Sip'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.port_page.port_list_tableWidget.setItem(i, 2, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Sport'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.port_page.port_list_tableWidget.setItem(i, 3, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Dip'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.port_page.port_list_tableWidget.setItem(i, 4, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Dport'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.port_page.port_list_tableWidget.setItem(i, 5, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Process'])
                newItem.setTextAlignment(Qt.AlignLeft)
                self.port_page.port_list_tableWidget.setItem(i, 6, newItem)

            tot = ret['Totle']
            # 设置当前页码
            self.port_page.port_list_now_label.setText(u"%d" %(self.port_page.port_list_now_page))

            # 设置总页数
            totpage = tot / MaxLines
            if (tot % MaxLines) > 0 :
                totpage += 1
            self.port_page.port_list_tot_page = totpage
            self.port_page.port_list_tot_label.setText(u"共 %d 页" %(totpage))
        else:
            QMessageBox.about(self, u"获取使用端口列表", u"错误:" + ret['ErrMsg'])        
