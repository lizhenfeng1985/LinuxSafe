# -*- coding: utf-8 -*-
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys  
import main
import urlpage
import http
import config
import gui_url
import gui_device
import gui_specrc

_encoding = QApplication.UnicodeUTF8

class GuiMain(QDialog,main.Ui_Form, gui_url.GuiUrl, gui_device.GuiDevice, gui_specrc.GuiSpecrc):  
    def __init__(self,parent=None):  
        super(GuiMain,self).__init__(parent)        
        self.setupUi(self)

        # 标题
        self.setWindowTitle(u"安全防护终端管理系统")
        # 去掉最大化
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        # 禁止拉伸窗口
        self.setFixedSize(self.width(), self.height())
        # 屏幕居中
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        
        # 设置左边列表栏目
        self.AddListLeft()
        # 设置底部版本号
        self.SetVersionBottom("2015.11.01")
        # url
        self.AddListLeftUrl()
        
        # 外设管理
        self.AddListLeftDevice()

        # 特殊资源管理
        self.AddListLeftSpecrc()        

        # 初始化界面配置
        self.InitConfig()
        
        
    def AddListLeft(self):
        self.listWidget_left.setGridSize(QSize(111, 25))        
        #self.listWidget_left.setIconSize(QSize(25,25))
        #self.listWidget_left.setViewMode(QListView.IconMode)
        #self.listWidget_left.insertItem(0, QListWidgetItem(QIcon("./image/bkg_blue.jpg"), "Url"))

        self.listWidget_left.insertItem(0, QListWidgetItem(u"    Url过滤"))
        self.listWidget_left.insertItem(1, QListWidgetItem(u"    外设管理"))        
        self.listWidget_left.insertItem(2, QListWidgetItem(u"    特殊资源"))
        self.listWidget_left.insertItem(3, QListWidgetItem(u"    防护日志"))
        #self.listWidget_left.insertItem(1, QListWidgetItem(u"    防火墙"))
        #self.listWidget_left.insertItem(2, QListWidgetItem(u"    外设管理"))
        #self.listWidget_left.insertItem(4, QListWidgetItem(u"    可信运行"))
        #self.listWidget_left.insertItem(5, QListWidgetItem(u"    进程防护"))
        #self.listWidget_left.insertItem(6, QListWidgetItem(u"    目录防护"))
        #self.listWidget_left.insertItem(1, QListWidgetItem(u"    系统设置"))

        self.connect(self.listWidget_left, SIGNAL("itemClicked (QListWidgetItem*)"), self.SelectLeftList)
        
    def SelectLeftList(self, Item=None):
        #QMessageBox.about(self, u"左侧列表", u"左侧列表")
        if Item==None:
            return
        #QMessageBox.about(self, Item.text(), Item.text())

    def SetVersionBottom(self, version):
        self.label_bottom_version.setText(main._translate("Form", "版本 : " + version, None))
        
    def InitConfig(self):
        # 获取配置信息
        url = "http://127.0.0.1:8080/config/get"
        ret = http.Post(url, {})
        if ret['ErrStat'] == 0:
            bWhite = ret['Config']['White_Start']
            bBlack = ret['Config']['Black_Start']
            if bWhite != 0:
                bWhite = 2
            if bBlack != 0:
                bBlack = 2
                
            config.GLB_CFG['URL']['White_Start'] = bWhite
            config.GLB_CFG['URL']['Black_Start'] = bBlack
            self.urlpage.urlpage_white_start_checkBox.setCheckState(bWhite)
            self.urlpage.urlpage_black_start_checkBox.setCheckState(bBlack)
            return 0
        else:
            QMessageBox.about(self, u"获取配置信息", u"获取配置信息:" + ret['ErrMsg'])
            return -1
        
app=QApplication(sys.argv)  
win=GuiMain()
win.show()
app.exec_()  
