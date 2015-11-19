# -*- coding: utf-8 -*-
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys  
import main
import log_ui
import http
import config

_encoding = QApplication.UnicodeUTF8

class GuiLog(QWidget):
    def __init__(self,parent=None):  
        super(GuiLog,self).__init__(parent)        
        self.setupUi(self)
        
    def AddListLeftLog(self):
        self.log_page = log_ui.LogPage()
        self.frame_mid_right.addWidget(self.log_page.log_tabWidget)
        self.connect(self.listWidget_left,SIGNAL("currentRowChanged(int)"),self.frame_mid_right,SLOT("setCurrentIndex(int)"))

        # 消息处理
        self.connect(self.log_page.log_url_first_btn, SIGNAL("clicked()"), self.LogPageUrl_First)
        self.connect(self.log_page.log_url_prev_btn, SIGNAL("clicked()"), self.LogPageUrl_Prev)
        self.connect(self.log_page.log_url_next_btn, SIGNAL("clicked()"), self.LogPageUrl_Next)
        self.connect(self.log_page.log_url_ok_btn, SIGNAL("clicked()"), self.LogPageUrl_OK)
        self.connect(self.log_page.log_url_query_btn, SIGNAL("clicked()"), self.LogPageUrl_Query)

    def LogPageUrl_First(self):
        self.log_page.log_url_now_page = 1
        self.LogPageUrl_SetList()

    def LogPageUrl_Prev(self):
        if self.log_page.log_url_now_page == 1:
            QMessageBox.about(self, u"获取URL日志", u"错误:已经是第一页")
        else:
            self.log_page.log_url_now_page -= 1
            self.LogPageUrl_SetList()

    def LogPageUrl_Next(self):
        if self.log_page.log_url_now_page == self.log_page.log_url_tot_page:
            QMessageBox.about(self, u"获取URL日志", u"错误:已经是第最后一页")
        else:
            self.log_page.log_url_now_page += 1
            self.LogPageUrl_SetList()

    def LogPageUrl_OK(self):
        try:
            jmpstr = self.log_page.log_url_jump_edit.text()
            jmpint = int(jmpstr)
            if jmpint < 1 or jmpint > self.log_page.log_url_tot_page:
                QMessageBox.about(self, u"获取URL日志", u"错误:页码输入错误")
            else:
                self.log_page.log_url_now_page = jmpint
                self.LogPageUrl_SetList()
        except:
            QMessageBox.about(self, u"获取URL日志", u"错误:页码输入错误")

    def LogPageUrl_Query(self):
        self.LogPageUrl_SetList()

    def LogPageUrl_SetList(self):
        MaxLines  = 10
        StartTime = self.log_page.log_url_start_timeedit.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        StopTime  = self.log_page.log_url_stop_timeedit.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        KeyWord   = self.log_page.log_url_query_edit.text().toUtf8()
    
        url = "%s/log/url/query" % (config.GLB_CFG['SRV_URL'])
        param = {'Start'     : (self.log_page.log_url_now_page - 1) * MaxLines,
                 'Length'    : MaxLines,
                 'StartTime' : StartTime,
                 'StopTime'  : StopTime,
                 'KeyWord'   : KeyWord,
                 }
        ret = http.Post(url, param)
        
        if ret['ErrStat'] == 0:
            # 清空列表
            for i in range(0, 10):
                for j in range(0, 8):
                    self.log_page.url_log_tableWidget.setItem(i, j, None)                
                
            # 添加列表
            for i in range(0, len(ret['Lists'])):
                newItem = QTableWidgetItem(ret['Lists'][i]['Type'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.url_log_tableWidget.setItem(i, 0, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Pid'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.url_log_tableWidget.setItem(i, 1, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['User'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.url_log_tableWidget.setItem(i, 2, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Subproc'])
                newItem.setTextAlignment(Qt.AlignLeft)
                self.log_page.url_log_tableWidget.setItem(i, 3, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Sipdip'])
                newItem.setTextAlignment(Qt.AlignLeft)
                self.log_page.url_log_tableWidget.setItem(i, 4, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Host'] + ret['Lists'][i]['Uri'])
                newItem.setTextAlignment(Qt.AlignLeft)
                self.log_page.url_log_tableWidget.setItem(i, 5, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Perm'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.url_log_tableWidget.setItem(i, 6, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Time'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.url_log_tableWidget.setItem(i, 7, newItem)

            tot = ret['Totle']
            # 设置当前页码
            self.log_page.log_url_now_label.setText(u"%d" %(self.log_page.log_url_now_page))

            # 设置总页数
            totpage = tot / MaxLines
            if (tot % MaxLines) > 0 :
                totpage += 1
            self.log_page.log_url_tot_page = totpage
            self.log_page.log_url_tot_label.setText(u"共 %d 页" %(totpage))
        else:
            QMessageBox.about(self, u"获取URL日志", u"错误:" + ret['ErrMsg'])
