# -*- coding: utf-8 -*-
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys  
import main
import urlpage
import http
import config

_encoding = QApplication.UnicodeUTF8

class GuiUrl(QWidget):
    def __init__(self,parent=None):  
        super(GuiUrl,self).__init__(parent)        
        self.setupUi(self)
        
    def AddListLeftUrl(self):
        self.urlpage_wdg = QTabWidget()        
        self.urlpage_wdg.setObjectName(u"urlpage")

        self.urlpage = urlpage.UrlPage()
        self.urlpage_wdg.addTab(self.urlpage.tbwhite, u"白名单")
        self.urlpage_wdg.addTab(self.urlpage.tbblack, u"黑名单")

        # 设置列表tabWidget中的值
        self.SetItemUrlWhite(self.urlpage.urlpage_white_tableWidget, 0, 10)
        self.SetItemUrlBlack(self.urlpage.urlpage_black_tableWidget, 0, 10)

        self.frame_mid_right.addWidget(self.urlpage_wdg)

        # 白名单 - 消息处理
        self.connect(self.urlpage.urlpage_white_add_btn, SIGNAL("clicked()"), self.UrlPageWhiteAdd)
        self.connect(self.urlpage.urlpage_white_del_btn, SIGNAL("clicked()"), self.UrlPageWhiteDel)
        self.connect(self.urlpage.urlpage_white_firstpage_btn, SIGNAL("clicked()"), self.UrlPageWhiteFirstPage)
        self.connect(self.urlpage.urlpage_white_prev_btn, SIGNAL("clicked()"), self.UrlPageWhitePrevPage)
        self.connect(self.urlpage.urlpage_white_next_btn, SIGNAL("clicked()"), self.UrlPageWhiteNextPage)
        self.connect(self.urlpage.urlpage_white_ok_btn, SIGNAL("clicked()"), self.UrlPageWhiteJump)
        self.connect(self.urlpage.urlpage_white_selectall_checkBox, SIGNAL("clicked()"), self.UrlPageWhiteSelectAll)
        self.connect(self.urlpage.urlpage_white_start_checkBox, SIGNAL("clicked()"), self.UrlPageWhiteCheckStart)

        # 黑名单 - 消息处理
        self.connect(self.urlpage.urlpage_black_add_btn, SIGNAL("clicked()"), self.UrlPageBlackAdd)
        self.connect(self.urlpage.urlpage_black_del_btn, SIGNAL("clicked()"), self.UrlPageBlackDel)
        self.connect(self.urlpage.urlpage_black_firstpage_btn, SIGNAL("clicked()"), self.UrlPageBlackFirstPage)
        self.connect(self.urlpage.urlpage_black_prev_btn, SIGNAL("clicked()"), self.UrlPageBlackPrevPage)
        self.connect(self.urlpage.urlpage_black_next_btn, SIGNAL("clicked()"), self.UrlPageBlackNextPage)
        self.connect(self.urlpage.urlpage_black_ok_btn, SIGNAL("clicked()"), self.UrlPageBlackJump)
        self.connect(self.urlpage.urlpage_black_selectall_checkBox, SIGNAL("clicked()"), self.UrlPageBlackSelectAll)
        self.connect(self.urlpage.urlpage_black_start_checkBox, SIGNAL("clicked()"), self.UrlPageBlackCheckStart)
        
        #label2=QLabel(u"这是窗口2!")
        #self.frame_mid_right.addWidget(label2)
        
        self.connect(self.listWidget_left,SIGNAL("currentRowChanged(int)"),self.frame_mid_right,SLOT("setCurrentIndex(int)"))

    # 白名单 - 填充Url列表
    def SetItemUrlWhite(self, qlistwidget, start, length):
        url = "http://127.0.0.1:8080/url/white/getlist"
        param = {'Start' : start, 'Length' : length}
        ret = http.Post(url, param)
        if ret['ErrStat'] == 0:
            # 清空列表
            for i in range(0, 10):
                qlistwidget.setItem(i, 0, None)
                qlistwidget.setItem(i, 1, None)
                
            # 添加列表
            for i in range(0, len(ret['Lists'])):
                newItem = QTableWidgetItem(ret['Lists'][i])
                newItem.setTextAlignment(Qt.AlignCenter)
                qlistwidget.setItem(i, 0, newItem)

                newItemChkbox = QTableWidgetItem()
                newItemChkbox.setCheckState(False)
                newItemChkbox.setTextAlignment(Qt.AlignCenter)
                qlistwidget.setItem(i, 1, newItemChkbox)

            tot = ret['Totle']
            # 设置当前页码
            self.urlpage.urlpage_white_nowpage_lab.setText(u"%d" %((start / 10) + 1))
            config.GLB_CFG['URL']['White_NowPage'] = (start / 10) + 1

            # 设置总页数
            totpage = tot / length
            if (tot % length) > 0 :
                totpage += 1
            self.urlpage.urlpage_white_totpage_lab.setText(u"共 %d 页" %(totpage))
            config.GLB_CFG['URL']['White_TotPage'] = totpage
        else:
            QMessageBox.about(self, u"获取URL列表", u"错误:" + ret['ErrMsg'])

    ## 白名单 - 启用 消息
    def UrlPageWhiteCheckStart(self):
        chkw = self.urlpage.urlpage_white_start_checkBox.checkState()
        chkb = self.urlpage.urlpage_black_start_checkBox.checkState()

        bsetw = 0
        bsetb = 0

        if chkw == 2 or chkw == 1: # 白选中
            chkw  = 2
            chkb  = 0
            bsetw = 1
            bsetb = 0
        else:
            pass

        url = "http://127.0.0.1:8080/config/set"
        param = {'WhiteStatus' : bsetw, 'BlackStatus' : bsetb}
        ret = http.Post(url, param)
        if ret['ErrStat'] == 0:
            # 更新数据
            config.GLB_CFG['URL']['White_Start'] = chkw
            config.GLB_CFG['URL']['Black_Start'] = chkb
            self.urlpage.urlpage_white_start_checkBox.setCheckState(chkw)
            self.urlpage.urlpage_black_start_checkBox.setCheckState(chkb)
            #QMessageBox.about(self, u"设置", u"设置:" + "white=%d" % (chkw) + "  black=%d" % (chkb))
        else:
            QMessageBox.about(self, u"设置", u"设置失败:" + ret['ErrMsg'])

    # 白名单 - 添加
    def UrlPageWhiteAdd(self):
        dialog = urlpage.UrlAddDialg()
        dialog.setModal(False)  
        dialog.exec_()
        if len(dialog.inputurl) < 1:
            QMessageBox.about(self, u"添加URL", u"添加失败:URL不能为空")
            return
        url = "http://127.0.0.1:8080/url/white/add"
        param = {'Url' : dialog.inputurl}
        ret = http.Post(url, param)
        if ret['ErrStat'] == 0:
            #QMessageBox.about(self, u"添加URL", u"添加成功")
            # 刷新列表
            self.SetItemUrlWhite(self.urlpage.urlpage_white_tableWidget, 0, 10)
        else:
            QMessageBox.about(self, u"添加URL", u"添加失败:" + ret['ErrMsg'])

    # 白名单 - 删除
    def UrlPageWhiteDel(self):
        itemcnt = self.urlpage.urlpage_white_tableWidget.rowCount()
        dellist = []

        for i in range(0, itemcnt):
            it = self.urlpage.urlpage_white_tableWidget.item(i, 1)
            if it == None:
                continue
            chk = it.checkState()
            if chk == 2: # 状态有0和2
                dellist.append(self.urlpage.urlpage_white_tableWidget.item(i, 0).text())
                
        url = "http://127.0.0.1:8080/url/white/del"
        for u in dellist:   
            param = {'Url' : u}
            ret = http.Post(url, param)
            if ret['ErrStat'] != 0:
                QMessageBox.about(self, u"删除URL", u"删除失败: %s\n" %(url) + ret['ErrMsg'])
        # 刷新列表
        self.SetItemUrlWhite(self.urlpage.urlpage_white_tableWidget, 0, 10)

    # 白名单 - 全选
    def UrlPageWhiteSelectAll(self):
        chk = self.urlpage.urlpage_white_selectall_checkBox.checkState()
        if chk == 0: #全不选
            itemcnt = self.urlpage.urlpage_white_tableWidget.rowCount()
            for i in range(0, itemcnt):
                it = self.urlpage.urlpage_white_tableWidget.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(False)
        elif chk == 2: #全选
            itemcnt = self.urlpage.urlpage_white_tableWidget.rowCount()
            for i in range(0, itemcnt):
                it = self.urlpage.urlpage_white_tableWidget.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(2)
        else:
            pass

    # 白名单 - 首页
    def UrlPageWhiteFirstPage(self):
        self.SetItemUrlWhite(self.urlpage.urlpage_white_tableWidget, 0, 10)

    # 白名单 - 上一页
    def UrlPageWhitePrevPage(self):
        nowpage = config.GLB_CFG['URL']['White_NowPage']
        if nowpage <= 1:
            QMessageBox.about(self, u"错误提示", u"已经是第一页")
            return
        self.SetItemUrlWhite(self.urlpage.urlpage_white_tableWidget, 10 * (nowpage - 2), 10)

    # 白名单 - 下一页
    def UrlPageWhiteNextPage(self):
        nowpage = config.GLB_CFG['URL']['White_NowPage']
        totpage = config.GLB_CFG['URL']['White_TotPage']
        if nowpage >= totpage:
            QMessageBox.about(self, u"错误提示", u"已经是最后一页")
            return
        self.SetItemUrlWhite(self.urlpage.urlpage_white_tableWidget, 10 * nowpage, 10)

    # 白名单 - 跳到        
    def UrlPageWhiteJump(self):
        pagestr = self.urlpage.urlpage_white_jump_lineEdit.text()
        totpage = config.GLB_CFG['URL']['White_TotPage']
        try:
            page = int(pagestr)
            if page < 1 or page > totpage:
                QMessageBox.about(self, u"错误提示", u"页码输入错误")
                return
        except:
            QMessageBox.about(self, u"错误提示", u"页码输入错误")
            return
        self.SetItemUrlWhite(self.urlpage.urlpage_white_tableWidget, 10 * (page - 1), 10)

    
    # 黑名单 - 填充Url列表
    def SetItemUrlBlack(self, qlistwidget, start, length):
        url = "http://127.0.0.1:8080/url/black/getlist"
        param = {'Start' : start, 'Length' : length}
        ret = http.Post(url, param)
        if ret['ErrStat'] == 0:
            # 清空列表
            for i in range(0, 10):
                qlistwidget.setItem(i, 0, None)
                qlistwidget.setItem(i, 1, None)
                
            # 添加列表
            for i in range(0, len(ret['Lists'])):
                newItem = QTableWidgetItem(ret['Lists'][i])
                newItem.setTextAlignment(Qt.AlignCenter)
                qlistwidget.setItem(i, 0, newItem)

                newItemChkbox = QTableWidgetItem()
                newItemChkbox.setCheckState(False)
                newItemChkbox.setTextAlignment(Qt.AlignCenter)
                qlistwidget.setItem(i, 1, newItemChkbox)

            tot = ret['Totle']
            # 设置当前页码
            self.urlpage.urlpage_black_nowpage_lab.setText(u"%d" %((start / 10) + 1))
            config.GLB_CFG['URL']['Black_NowPage'] = (start / 10) + 1

            # 设置总页数
            totpage = tot / length
            if (tot % length) > 0 :
                totpage += 1
            self.urlpage.urlpage_black_totpage_lab.setText(u"共 %d 页" %(totpage))
            config.GLB_CFG['URL']['Black_TotPage'] = totpage
        else:
            QMessageBox.about(self, u"获取URL列表", u"错误:" + ret['ErrMsg'])
    
    ## 黑名单启用 消息
    def UrlPageBlackCheckStart(self):
        chkw = self.urlpage.urlpage_white_start_checkBox.checkState()
        chkb = self.urlpage.urlpage_black_start_checkBox.checkState()

        bsetw = 0
        bsetb = 0

        if chkb == 2 or chkb == 1: # 黑选中
            chkb  = 2
            chkw  = 0
            bsetb = 1
            bsetw = 0
        else:
            pass
            
        url = "http://127.0.0.1:8080/config/set"
        param = {'WhiteStatus' : bsetw, 'BlackStatus' : bsetb}
        ret = http.Post(url, param)
        if ret['ErrStat'] == 0:
            # 更新数据
            config.GLB_CFG['URL']['White_Start'] = chkw
            config.GLB_CFG['URL']['Black_Start'] = chkb
            self.urlpage.urlpage_white_start_checkBox.setCheckState(chkw)
            self.urlpage.urlpage_black_start_checkBox.setCheckState(chkb)
            #QMessageBox.about(self, u"设置", u"设置:" + "white=%d" % (chkw) + "  black=%d" % (chkb))
        else:
            QMessageBox.about(self, u"设置", u"设置失败:" + ret['ErrMsg'])


    # 黑名单 - 添加
    def UrlPageBlackAdd(self):
        dialog = urlpage.UrlAddDialg()
        dialog.setModal(False)  
        dialog.exec_()
        if len(dialog.inputurl) < 1:
            QMessageBox.about(self, u"添加URL", u"添加失败:URL不能为空")
            return
        url = "http://127.0.0.1:8080/url/black/add"
        param = {'Url' : dialog.inputurl}
        ret = http.Post(url, param)
        if ret['ErrStat'] == 0:
            #QMessageBox.about(self, u"添加URL", u"添加成功")
            # 刷新列表
            self.SetItemUrlBlack(self.urlpage.urlpage_black_tableWidget, 0, 10)
        else:
            QMessageBox.about(self, u"添加URL", u"添加失败:" + ret['ErrMsg'])

    # 黑名单 - 删除
    def UrlPageBlackDel(self):
        itemcnt = self.urlpage.urlpage_black_tableWidget.rowCount()
        dellist = []

        for i in range(0, itemcnt):
            it = self.urlpage.urlpage_black_tableWidget.item(i, 1)
            if it == None:
                continue
            chk = it.checkState()
            if chk == 2: # 状态有0和2
                dellist.append(self.urlpage.urlpage_black_tableWidget.item(i, 0).text())
                
        url = "http://127.0.0.1:8080/url/black/del"
        for u in dellist:   
            param = {'Url' : u}
            ret = http.Post(url, param)
            if ret['ErrStat'] != 0:
                QMessageBox.about(self, u"删除URL", u"删除失败: %s\n" %(url) + ret['ErrMsg'])
        # 刷新列表
        self.SetItemUrlBlack(self.urlpage.urlpage_black_tableWidget, 0, 10)

    # 黑名单 - 全选
    def UrlPageBlackSelectAll(self):
        chk = self.urlpage.urlpage_black_selectall_checkBox.checkState()
        if chk == 0: #全不选
            itemcnt = self.urlpage.urlpage_black_tableWidget.rowCount()
            for i in range(0, itemcnt):
                it = self.urlpage.urlpage_black_tableWidget.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(False)
        elif chk == 2: #全选
            itemcnt = self.urlpage.urlpage_black_tableWidget.rowCount()
            for i in range(0, itemcnt):
                it = self.urlpage.urlpage_black_tableWidget.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(2)
        else:
            pass

    # 黑名单 - 首页
    def UrlPageBlackFirstPage(self):
        self.SetItemUrlBlack(self.urlpage.urlpage_black_tableWidget, 0, 10)

    # 黑名单 - 上一页
    def UrlPageBlackPrevPage(self):
        nowpage = config.GLB_CFG['URL']['Black_NowPage']
        if nowpage <= 1:
            QMessageBox.about(self, u"错误提示", u"已经是第一页")
            return
        self.SetItemUrlBlack(self.urlpage.urlpage_black_tableWidget, 10 * (nowpage - 2), 10)

    # 黑名单 - 下一页
    def UrlPageBlackNextPage(self):
        nowpage = config.GLB_CFG['URL']['Black_NowPage']
        totpage = config.GLB_CFG['URL']['Black_TotPage']
        if nowpage >= totpage:
            QMessageBox.about(self, u"错误提示", u"已经是最后一页")
            return
        self.SetItemUrlBlack(self.urlpage.urlpage_black_tableWidget, 10 * nowpage, 10)

    # 黑名单 - 跳到        
    def UrlPageBlackJump(self):
        pagestr = self.urlpage.urlpage_black_jump_lineEdit.text()
        totpage = config.GLB_CFG['URL']['Black_TotPage']
        try:
            page = int(pagestr)
            if page < 1 or page > totpage:
                QMessageBox.about(self, u"错误提示", u"页码输入错误")
                return
        except:
            QMessageBox.about(self, u"错误提示", u"页码输入错误")
            return
        self.SetItemUrlBlack(self.urlpage.urlpage_black_tableWidget, 10 * (page - 1), 10)
        
    
