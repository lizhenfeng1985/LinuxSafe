# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'utlpage.ui'
#
# Created: Fri Oct 30 14:36:19 2015
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
    
     
class UrlPage(QtGui.QWidget):  
    def __init__(self,parent=None):  
        super(UrlPage,self).__init__(parent)
        
        # 添加标签
        self.CreateUrlWhite()        
        self.CreateUrlBlack()
            
    def CreateUrlWhite(self): 
        # 白名单
        self.tbwhite = QtGui.QListWidget()
        self.tbwhite.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tbwhite.setFrameShadow(QtGui.QFrame.Raised)
        self.tbwhite.setObjectName(_fromUtf8("urlpage_white"))

        url_white_lab1 = QtGui.QLabel(self.tbwhite)
        url_white_lab1.setGeometry(QtCore.QRect(18, 15, 381, 16))
        url_white_lab1.setObjectName(_fromUtf8("url_white_lab1"))
        url_white_lab1.setText(_translate("Form", "仅允许访问列表中的URL，黑名单和白名单只能启用一个", None))

        self.urlpage_white_start_checkBox = QtGui.QCheckBox(self.tbwhite)
        self.urlpage_white_start_checkBox.setGeometry(QtCore.QRect(18, 38, 101, 23))
        self.urlpage_white_start_checkBox.setObjectName(_fromUtf8("urlpage_white_start_checkBox"))
        self.urlpage_white_start_checkBox.setText(_translate("Form", "启用白名单", None))

        self.urlpage_white_add_btn = QtGui.QPushButton(self.tbwhite)
        self.urlpage_white_add_btn.setGeometry(QtCore.QRect(520, 38, 45, 23))
        self.urlpage_white_add_btn.setObjectName(_fromUtf8("urlpage_white_add_btn"))
        self.urlpage_white_add_btn.setText(_translate("Form", "添加", None))
        self.urlpage_white_add_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        
        self.urlpage_white_del_btn = QtGui.QPushButton(self.tbwhite)
        self.urlpage_white_del_btn.setGeometry(QtCore.QRect(570, 38, 45, 23))
        self.urlpage_white_del_btn.setObjectName(_fromUtf8("urlpage_white_del_btn"))
        self.urlpage_white_del_btn.setText(_translate("Form", "删除", None))
        self.urlpage_white_del_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))

        self.urlpage_white_tableWidget = QtGui.QTableWidget(self.tbwhite)
        self.urlpage_white_tableWidget.setGeometry(QtCore.QRect(10, 64, 611, 251))
        self.urlpage_white_tableWidget.setObjectName(_fromUtf8("urlpage_white_tableWidget"))
        self.urlpage_white_tableWidget.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.urlpage_white_tableWidget.verticalHeader().setVisible(False)
        self.urlpage_white_tableWidget.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.urlpage_white_tableWidget.setAlternatingRowColors(True)
        self.urlpage_white_tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.urlpage_white_tableWidget.setRowCount(10)
        self.urlpage_white_tableWidget.setColumnCount(2)
        self.urlpage_white_tableWidget.setHorizontalHeaderLabels([_fromUtf8("URL地址"),_fromUtf8("选择")])
        self.urlpage_white_tableWidget.setShowGrid(False)
        self.urlpage_white_tableWidget.setColumnWidth(0,568)
        self.urlpage_white_tableWidget.setColumnWidth(1,40)
        
        # 循环添加
        for i in range(0, 10):
            self.urlpage_white_tableWidget.setRowHeight(i,21)
            
        self.urlpage_white_firstpage_btn = QtGui.QPushButton(self.tbwhite)
        self.urlpage_white_firstpage_btn.setGeometry(QtCore.QRect(10, 320, 62, 23))
        self.urlpage_white_firstpage_btn.setObjectName(_fromUtf8("urlpage_white_firstpage_btn"))
        self.urlpage_white_firstpage_btn.setText(_translate("Form", "首页", None))
        self.urlpage_white_firstpage_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))

        self.urlpage_white_prev_btn = QtGui.QPushButton(self.tbwhite)
        self.urlpage_white_prev_btn.setGeometry(QtCore.QRect(77, 320, 62, 23))
        self.urlpage_white_prev_btn.setObjectName(_fromUtf8("urlpage_white_prev_btn"))
        self.urlpage_white_prev_btn.setText(_translate("Form", "上一页", None))
        self.urlpage_white_prev_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))

        self.urlpage_white_nowpage_lab = QtGui.QLabel(self.tbwhite)
        self.urlpage_white_nowpage_lab.setGeometry(QtCore.QRect(144, 320, 30, 23))
        self.urlpage_white_nowpage_lab.setObjectName(_fromUtf8("urlpage_white_nowpage_lab"))
        self.urlpage_white_nowpage_lab.setText(_translate("Form", "1", None))
        self.urlpage_white_nowpage_lab.setAlignment(QtCore.Qt.AlignCenter)
        
        self.urlpage_white_next_btn = QtGui.QPushButton(self.tbwhite)
        self.urlpage_white_next_btn.setGeometry(QtCore.QRect(179, 320, 62, 23))
        self.urlpage_white_next_btn.setObjectName(_fromUtf8("urlpage_white_next_btn"))
        self.urlpage_white_next_btn.setText(_translate("Form", "下一页", None))
        self.urlpage_white_next_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))

        self.urlpage_white_totpage_lab = QtGui.QLabel(self.tbwhite)
        self.urlpage_white_totpage_lab.setGeometry(QtCore.QRect(255, 320, 70, 23))
        self.urlpage_white_totpage_lab.setObjectName(_fromUtf8("urlpage_white_totpage_lab"))
        self.urlpage_white_totpage_lab.setText(_translate("Form", "共0页", None))
        self.urlpage_white_totpage_lab.setAlignment(QtCore.Qt.AlignCenter)
        
        self.url_white_lab_jmp = QtGui.QLabel(self.tbwhite)
        self.url_white_lab_jmp.setGeometry(QtCore.QRect(334, 320, 24, 23))
        self.url_white_lab_jmp.setObjectName(_fromUtf8("label_3"))
        self.url_white_lab_jmp.setText(_translate("Form", "跳到", None))
        self.url_white_lab_jmp.setAlignment(QtCore.Qt.AlignCenter)

        self.urlpage_white_jump_lineEdit = QtGui.QLineEdit(self.tbwhite)
        self.urlpage_white_jump_lineEdit.setGeometry(QtCore.QRect(363, 320, 51, 23))
        self.urlpage_white_jump_lineEdit.setObjectName(_fromUtf8("urlpage_white_jump_lineEdit"))
        self.urlpage_white_jump_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.urlpage_white_jump_lineEdit.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.urlpage_white_jump_lineEdit.setText(_translate("Form", "1", None))        

        self.urlpage_white_ok_btn = QtGui.QPushButton(self.tbwhite)
        self.urlpage_white_ok_btn.setGeometry(QtCore.QRect(420, 320, 75, 23))
        self.urlpage_white_ok_btn.setObjectName(_fromUtf8("urlpage_white_ok_btn"))
        self.urlpage_white_ok_btn.setText(_translate("Form", "确定", None))
        self.urlpage_white_ok_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        
        self.urlpage_white_selectall_checkBox = QtGui.QCheckBox(self.tbwhite)
        self.urlpage_white_selectall_checkBox.setGeometry(QtCore.QRect(570, 320, 47, 23))
        self.urlpage_white_selectall_checkBox.setObjectName(_fromUtf8("urlpage_white_selectall_checkBox"))
        self.urlpage_white_selectall_checkBox.setText(_translate("Form", "全选", None))

        return self.tbwhite

    def CreateUrlBlack(self):
        # 黑名单
        self.tbblack = QtGui.QListWidget()
        self.tbblack.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tbblack.setFrameShadow(QtGui.QFrame.Raised)
        self.tbblack.setObjectName(_fromUtf8("urlpage_black"))

        url_black_lab1 = QtGui.QLabel(self.tbblack)
        url_black_lab1.setGeometry(QtCore.QRect(18, 15, 381, 16))
        url_black_lab1.setObjectName(_fromUtf8("url_black_lab1"))
        url_black_lab1.setText(_translate("Form", "不允许访问列表中的URL，黑名单和白名单只能启用一个", None))

        self.urlpage_black_start_checkBox = QtGui.QCheckBox(self.tbblack)
        self.urlpage_black_start_checkBox.setGeometry(QtCore.QRect(18, 38, 101, 23))
        self.urlpage_black_start_checkBox.setObjectName(_fromUtf8("urlpage_black_start_checkBox"))
        self.urlpage_black_start_checkBox.setText(_translate("Form", "启用黑名单", None))

        self.urlpage_black_add_btn = QtGui.QPushButton(self.tbblack)
        self.urlpage_black_add_btn.setGeometry(QtCore.QRect(520, 38, 45, 23))
        self.urlpage_black_add_btn.setObjectName(_fromUtf8("urlpage_black_add_btn"))
        self.urlpage_black_add_btn.setText(_translate("Form", "添加", None))
        self.urlpage_black_add_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        
        self.urlpage_black_del_btn = QtGui.QPushButton(self.tbblack)
        self.urlpage_black_del_btn.setGeometry(QtCore.QRect(570, 38, 45, 23))
        self.urlpage_black_del_btn.setObjectName(_fromUtf8("urlpage_black_del_btn"))
        self.urlpage_black_del_btn.setText(_translate("Form", "删除", None))
        self.urlpage_black_del_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))

        self.urlpage_black_tableWidget = QtGui.QTableWidget(self.tbblack)
        self.urlpage_black_tableWidget.setGeometry(QtCore.QRect(10, 64, 611, 251))
        self.urlpage_black_tableWidget.setObjectName(_fromUtf8("urlpage_black_tableWidget"))
        self.urlpage_black_tableWidget.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.urlpage_black_tableWidget.verticalHeader().setVisible(False)
        self.urlpage_black_tableWidget.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.urlpage_black_tableWidget.setAlternatingRowColors(True)
        self.urlpage_black_tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.urlpage_black_tableWidget.setRowCount(10)
        self.urlpage_black_tableWidget.setColumnCount(2)
        self.urlpage_black_tableWidget.setHorizontalHeaderLabels([_fromUtf8("URL地址"),_fromUtf8("选择")])
        self.urlpage_black_tableWidget.setShowGrid(False)
        self.urlpage_black_tableWidget.setColumnWidth(0,568)
        self.urlpage_black_tableWidget.setColumnWidth(1,40)
        
        # 循环添加
        for i in range(0, 10):
            self.urlpage_black_tableWidget.setRowHeight(i,21)
            
        self.urlpage_black_firstpage_btn = QtGui.QPushButton(self.tbblack)
        self.urlpage_black_firstpage_btn.setGeometry(QtCore.QRect(10, 320, 62, 23))
        self.urlpage_black_firstpage_btn.setObjectName(_fromUtf8("urlpage_black_firstpage_btn"))
        self.urlpage_black_firstpage_btn.setText(_translate("Form", "首页", None))
        self.urlpage_black_firstpage_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))

        self.urlpage_black_prev_btn = QtGui.QPushButton(self.tbblack)
        self.urlpage_black_prev_btn.setGeometry(QtCore.QRect(77, 320, 62, 23))
        self.urlpage_black_prev_btn.setObjectName(_fromUtf8("urlpage_black_prev_btn"))
        self.urlpage_black_prev_btn.setText(_translate("Form", "上一页", None))
        self.urlpage_black_prev_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))

        self.urlpage_black_nowpage_lab = QtGui.QLabel(self.tbblack)
        self.urlpage_black_nowpage_lab.setGeometry(QtCore.QRect(144, 320, 30, 23))
        self.urlpage_black_nowpage_lab.setObjectName(_fromUtf8("urlpage_black_nowpage_lab"))
        self.urlpage_black_nowpage_lab.setText(_translate("Form", "1", None))
        self.urlpage_black_nowpage_lab.setAlignment(QtCore.Qt.AlignCenter)
        
        self.urlpage_black_next_btn = QtGui.QPushButton(self.tbblack)
        self.urlpage_black_next_btn.setGeometry(QtCore.QRect(179, 320, 62, 23))
        self.urlpage_black_next_btn.setObjectName(_fromUtf8("urlpage_black_next_btn"))
        self.urlpage_black_next_btn.setText(_translate("Form", "下一页", None))
        self.urlpage_black_next_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))

        self.urlpage_black_totpage_lab = QtGui.QLabel(self.tbblack)
        self.urlpage_black_totpage_lab.setGeometry(QtCore.QRect(255, 320, 70, 23))
        self.urlpage_black_totpage_lab.setObjectName(_fromUtf8("urlpage_black_totpage_lab"))
        self.urlpage_black_totpage_lab.setText(_translate("Form", "共0页", None))
        self.urlpage_black_totpage_lab.setAlignment(QtCore.Qt.AlignCenter)
        
        self.url_black_lab_jmp = QtGui.QLabel(self.tbblack)
        self.url_black_lab_jmp.setGeometry(QtCore.QRect(334, 320, 24, 23))
        self.url_black_lab_jmp.setObjectName(_fromUtf8("label_3"))
        self.url_black_lab_jmp.setText(_translate("Form", "跳到", None))
        self.url_black_lab_jmp.setAlignment(QtCore.Qt.AlignCenter)

        self.urlpage_black_jump_lineEdit = QtGui.QLineEdit(self.tbblack)
        self.urlpage_black_jump_lineEdit.setGeometry(QtCore.QRect(363, 320, 51, 23))
        self.urlpage_black_jump_lineEdit.setObjectName(_fromUtf8("urlpage_black_jump_lineEdit"))
        self.urlpage_black_jump_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.urlpage_black_jump_lineEdit.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        self.urlpage_black_jump_lineEdit.setText(_translate("Form", "1", None))        

        self.urlpage_black_ok_btn = QtGui.QPushButton(self.tbblack)
        self.urlpage_black_ok_btn.setGeometry(QtCore.QRect(420, 320, 75, 23))
        self.urlpage_black_ok_btn.setObjectName(_fromUtf8("urlpage_black_ok_btn"))
        self.urlpage_black_ok_btn.setText(_translate("Form", "确定", None))
        self.urlpage_black_ok_btn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        
        self.urlpage_black_selectall_checkBox = QtGui.QCheckBox(self.tbblack)
        self.urlpage_black_selectall_checkBox.setGeometry(QtCore.QRect(570, 320, 47, 23))
        self.urlpage_black_selectall_checkBox.setObjectName(_fromUtf8("urlpage_black_selectall_checkBox"))
        self.urlpage_black_selectall_checkBox.setText(_translate("Form", "全选", None))
        return self.tbblack

# Url添加 删除弹出对话框
class UrlAddDialg(QtGui.QDialog):  
    def __init__(self,parent=None):  
        QtGui.QWidget.__init__(self)  
        self.resize(380,58)  
        # 标题
        self.setWindowTitle(u"输入URL")
        # 去掉最大化
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        # 禁止拉伸窗口
        self.setFixedSize(self.width(), self.height())        

        self.lineedit = QtGui.QLineEdit(self)
        self.lineedit.setGeometry(QtCore.QRect(20, 20, 250, 23))
        self.lineedit.setObjectName(_fromUtf8("inputurl"))
        self.lineedit.setAlignment(QtCore.Qt.AlignLeft)
        self.lineedit.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        #lineedit.setText(_translate("Form", "", "输入URL"))

        okbtn = QtGui.QPushButton(self)
        okbtn.setGeometry(QtCore.QRect(290, 20, 75, 23))
        okbtn.setObjectName(_fromUtf8("inputurl"))
        okbtn.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_btn.jpg);"))
        okbtn.setText(_fromUtf8("确认"))

        self.inputurl = ""
        self.connect(okbtn,QtCore.SIGNAL('clicked()'),self.getUrl)
        self.connect(okbtn, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('close()'))

    def getUrl(self):
        self.inputurl = self.lineedit.text()
        
        
        

        
        
        
