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

        self.connect(self.log_page.log_device_first_btn, SIGNAL("clicked()"), self.LogPageDevice_First)
        self.connect(self.log_page.log_device_prev_btn, SIGNAL("clicked()"), self.LogPageDevice_Prev)
        self.connect(self.log_page.log_device_next_btn, SIGNAL("clicked()"), self.LogPageDevice_Next)
        self.connect(self.log_page.log_device_ok_btn, SIGNAL("clicked()"), self.LogPageDevice_OK)
        self.connect(self.log_page.log_device_query_btn, SIGNAL("clicked()"), self.LogPageDevice_Query)

        self.connect(self.log_page.log_specrc_first_btn, SIGNAL("clicked()"), self.LogPageSpecrc_First)
        self.connect(self.log_page.log_specrc_prev_btn, SIGNAL("clicked()"), self.LogPageSpecrc_Prev)
        self.connect(self.log_page.log_specrc_next_btn, SIGNAL("clicked()"), self.LogPageSpecrc_Next)
        self.connect(self.log_page.log_specrc_ok_btn, SIGNAL("clicked()"), self.LogPageSpecrc_OK)
        self.connect(self.log_page.log_specrc_query_btn, SIGNAL("clicked()"), self.LogPageSpecrc_Query)

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

    # 外设管理
    def LogPageDevice_First(self):
        self.log_page.log_device_now_page = 1
        self.LogPageDevice_SetList()

    def LogPageDevice_Prev(self):
        if self.log_page.log_device_now_page == 1:
            QMessageBox.about(self, u"获取外设管理日志", u"错误:已经是第一页")
        else:
            self.log_page.log_device_now_page -= 1
            self.LogPageDevice_SetList()

    def LogPageDevice_Next(self):
        if self.log_page.log_device_now_page == self.log_page.log_device_tot_page:
            QMessageBox.about(self, u"获取外设管理日志", u"错误:已经是第最后一页")
        else:
            self.log_page.log_device_now_page += 1
            self.LogPageDevice_SetList()

    def LogPageDevice_OK(self):
        try:
            jmpstr = self.log_page.log_device_jump_edit.text()
            jmpint = int(jmpstr)

            if jmpint < 1 or jmpint > self.log_page.log_device_tot_page:
                QMessageBox.about(self, u"获取外设管理日志", u"错误:页码输入错误")
            else:
                self.log_page.log_device_now_page = jmpint
                self.LogPageDevice_SetList()
        except:
            QMessageBox.about(self, u"获取外设管理日志", u"错误:页码输入错误")

    def LogPageDevice_Query(self):
        self.LogPageDevice_SetList()

    def LogPageDevice_SetList(self):
        MaxLines  = 10
        StartTime = self.log_page.log_device_start_timeedit.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        StopTime  = self.log_page.log_device_stop_timeedit.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        KeyWord   = self.log_page.log_device_query_edit.text().toUtf8()
    
        url = "%s/log/device/query" % (config.GLB_CFG['SRV_URL'])
        param = {'Start'     : (self.log_page.log_device_now_page - 1) * MaxLines,
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
                    self.log_page.device_log_tableWidget.setItem(i, j, None)                
                
            # 添加列表
            for i in range(0, len(ret['Lists'])):
                newItem = QTableWidgetItem(ret['Lists'][i]['Type'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.device_log_tableWidget.setItem(i, 0, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Pid'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.device_log_tableWidget.setItem(i, 1, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['User'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.device_log_tableWidget.setItem(i, 2, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Subproc'])
                newItem.setTextAlignment(Qt.AlignLeft)
                self.log_page.device_log_tableWidget.setItem(i, 3, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['ObjSrc'])
                newItem.setTextAlignment(Qt.AlignLeft)
                self.log_page.device_log_tableWidget.setItem(i, 4, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Perm'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.device_log_tableWidget.setItem(i, 5, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Time'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.device_log_tableWidget.setItem(i, 6, newItem)

            tot = ret['Totle']
            # 设置当前页码
            self.log_page.log_device_now_label.setText(u"%d" %(self.log_page.log_device_now_page))

            # 设置总页数
            totpage = tot / MaxLines
            if (tot % MaxLines) > 0 :
                totpage += 1
            self.log_page.log_device_tot_page = totpage
            self.log_page.log_device_tot_label.setText(u"共 %d 页" %(totpage))
        else:
            QMessageBox.about(self, u"获取外设管理日志", u"错误:" + ret['ErrMsg'])

    # 特殊资源管理
    def LogPageSpecrc_First(self):
        self.log_page.log_specrc_now_page = 1
        self.LogPageSpecrc_SetList()

    def LogPageSpecrc_Prev(self):
        if self.log_page.log_specrc_now_page == 1:
            QMessageBox.about(self, u"获取特殊资源管理日志", u"错误:已经是第一页")
        else:
            self.log_page.log_specrc_now_page -= 1
            self.LogPageSpecrc_SetList()

    def LogPageSpecrc_Next(self):
        if self.log_page.log_specrc_now_page == self.log_page.log_specrc_tot_page:
            QMessageBox.about(self, u"获取特殊资源管理日志", u"错误:已经是第最后一页")
        else:
            self.log_page.log_specrc_now_page += 1
            self.LogPageSpecrc_SetList()

    def LogPageSpecrc_OK(self):
        try:
            jmpstr = self.log_page.log_specrc_jump_edit.text()
            jmpint = int(jmpstr)

            if jmpint < 1 or jmpint > self.log_page.log_specrc_tot_page:
                QMessageBox.about(self, u"获取特殊资源管理日志", u"错误:页码输入错误")
            else:
                self.log_page.log_specrc_now_page = jmpint
                self.LogPageSpecrc_SetList()
        except:
            QMessageBox.about(self, u"获取特殊资源管理日志", u"错误:页码输入错误")

    def LogPageSpecrc_Query(self):
        self.LogPageSpecrc_SetList()

    def LogPageSpecrc_SetList(self):
        MaxLines  = 10
        StartTime = self.log_page.log_specrc_start_timeedit.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        StopTime  = self.log_page.log_specrc_stop_timeedit.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        KeyWord   = self.log_page.log_specrc_query_edit.text().toUtf8()
    
        url = "%s/log/specrc/query" % (config.GLB_CFG['SRV_URL'])
        param = {'Start'     : (self.log_page.log_specrc_now_page - 1) * MaxLines,
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
                    self.log_page.specrc_log_tableWidget.setItem(i, j, None)                
                
            # 添加列表
            for i in range(0, len(ret['Lists'])):
                newItem = QTableWidgetItem(ret['Lists'][i]['Type'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.specrc_log_tableWidget.setItem(i, 0, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Pid'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.specrc_log_tableWidget.setItem(i, 1, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['User'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.specrc_log_tableWidget.setItem(i, 2, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Subproc'])
                newItem.setTextAlignment(Qt.AlignLeft)
                self.log_page.specrc_log_tableWidget.setItem(i, 3, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['ObjSrc'])
                newItem.setTextAlignment(Qt.AlignLeft)
                self.log_page.specrc_log_tableWidget.setItem(i, 4, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Perm'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.specrc_log_tableWidget.setItem(i, 5, newItem)

                newItem = QTableWidgetItem(ret['Lists'][i]['Time'])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.log_page.specrc_log_tableWidget.setItem(i, 6, newItem)

            tot = ret['Totle']
            # 设置当前页码
            self.log_page.log_specrc_now_label.setText(u"%d" %(self.log_page.log_specrc_now_page))

            # 设置总页数
            totpage = tot / MaxLines
            if (tot % MaxLines) > 0 :
                totpage += 1
            self.log_page.log_specrc_tot_page = totpage
            self.log_page.log_specrc_tot_label.setText(u"共 %d 页" %(totpage))
        else:
            QMessageBox.about(self, u"获取特殊资源管理日志", u"错误:" + ret['ErrMsg'])
