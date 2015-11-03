# -*- coding: utf-8 -*-
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys  
import main
import urlpage
import http

_encoding = QApplication.UnicodeUTF8

class GuiMain(QDialog,main.Ui_Form):  
    def __init__(self,parent=None):  
        super(GuiMain,self).__init__(parent)        
        self.setupUi(self)

        # 标题
        self.setWindowTitle(u"安全防护终端管理系统")
        # 去掉最大化
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        # 禁止拉伸窗口
        self.setFixedSize(self.width(), self.height())
        # 设置左边列表栏目
        self.AddListLeft()
        # 设置底部版本号
        self.SetVersionBottom("2015.11.01")

        # url
        self.AddListLeftUrl()
        
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

        # 消息处理
        self.connect(self.urlpage.urlpage_white_add_btn, SIGNAL("clicked()"), self.UrlPageWhiteAdd)
        self.connect(self.urlpage.urlpage_white_del_btn, SIGNAL("clicked()"), self.UrlPageWhiteDel)
        self.connect(self.urlpage.urlpage_white_firstpage_btn, SIGNAL("clicked()"), self.UrlPageWhiteFirstPage)
        self.connect(self.urlpage.urlpage_white_prev_btn, SIGNAL("clicked()"), self.UrlPageWhitePrevPage)
        self.connect(self.urlpage.urlpage_white_next_btn, SIGNAL("clicked()"), self.UrlPageWhiteNextPage)
        self.connect(self.urlpage.urlpage_white_ok_btn, SIGNAL("clicked()"), self.UrlPageWhiteJump)


        
        label2=QLabel(u"这是窗口2!")
        self.frame_mid_right.addWidget(label2)
        
        self.connect(self.listWidget_left,SIGNAL("currentRowChanged(int)"),self.frame_mid_right,SLOT("setCurrentIndex(int)"))
        
        
    def AddListLeft(self):
        self.listWidget_left.setGridSize(QSize(111, 25))        
        #self.listWidget_left.setIconSize(QSize(25,25))
        #self.listWidget_left.setViewMode(QListView.IconMode)
        #self.listWidget_left.insertItem(0, QListWidgetItem(QIcon("./image/bkg_blue.jpg"), "Url"))

        self.listWidget_left.insertItem(0, QListWidgetItem(u"    Url过滤"))
        self.listWidget_left.insertItem(1, QListWidgetItem(u"    防火墙"))
        self.listWidget_left.insertItem(2, QListWidgetItem(u"    外设管理"))
        self.listWidget_left.insertItem(3, QListWidgetItem(u"    特殊资源"))
        self.listWidget_left.insertItem(4, QListWidgetItem(u"    可信运行"))
        self.listWidget_left.insertItem(5, QListWidgetItem(u"    进程防护"))
        self.listWidget_left.insertItem(6, QListWidgetItem(u"    目录防护"))
        self.listWidget_left.insertItem(7, QListWidgetItem(u"    系统设置"))
        self.listWidget_left.insertItem(8, QListWidgetItem(u"    防护日志"))

        self.connect(self.listWidget_left, SIGNAL("itemClicked (QListWidgetItem*)"), self.SelectLeftList)


    def SetVersionBottom(self, version):
        self.label_bottom_version.setText(main._translate("Form", "版本 : " + version, None))

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
        else:
            QMessageBox.about(self, u"获取URL列表", u"错误:" + ret['ErrMsg'])

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
        else:
            QMessageBox.about(self, u"获取URL列表", u"错误:" + ret['ErrMsg'])

    def UrlPageWhiteAdd(self):
        dialog = urlpage.UrlAddDialg()
        dialog.setModal(False)  
        dialog.exec_()
        url = "http://127.0.0.1:8080/url/white/add"
        param = {'Url' : dialog.inputurl}
        ret = http.Post(url, param)
        if ret['ErrStat'] == 0:
            #QMessageBox.about(self, u"添加URL", u"添加成功")
            # 刷新列表
            self.SetItemUrlWhite(self.urlpage.urlpage_white_tableWidget, 0, 10)
        else:
            QMessageBox.about(self, u"添加URL", u"添加失败:" + ret['ErrMsg'])

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

    def UrlPageWhiteFirstPage(self):
        QMessageBox.about(self, u"白名单", u"首页")

    def UrlPageWhitePrevPage(self):
        QMessageBox.about(self, u"白名单", u"上一页")

    def UrlPageWhiteNextPage(self):
        QMessageBox.about(self, u"白名单", u"下一页")

    def UrlPageWhiteJump(self):
        QMessageBox.about(self, u"白名单", u"跳转")


    def SelectLeftList(self, Item=None):
        QMessageBox.about(self, u"左侧列表", u"左侧列表")
        if Item==None:
            return
        QMessageBox.about(self, Item.text(), Item.text())
        
app=QApplication(sys.argv)  
win=GuiMain()  
win.show()  
app.exec_()  
