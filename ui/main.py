# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(747, 510)
        # 全局背景
        self.frame_bkground = QtGui.QFrame(Form)
        self.frame_bkground.setGeometry(QtCore.QRect(0, 0, 751, 511))
        self.frame_bkground.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_white.jpg);"))
        self.frame_bkground.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_bkground.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_bkground.setObjectName(_fromUtf8("frame_bkground"))

        # 顶部背景
        self.frame_top = QtGui.QFrame(self.frame_bkground)
        self.frame_top.setGeometry(QtCore.QRect(0, 0, 751, 111))
        self.frame_top.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_blue.jpg);"))
        self.frame_top.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_top.setObjectName(_fromUtf8("frame_top"))

        # 顶部logo
        self.frame_top_logo = QtGui.QFrame(self.frame_top)
        self.frame_top_logo.setGeometry(QtCore.QRect(30, 10, 90, 90))
        self.frame_top_logo.setStyleSheet(_fromUtf8("border-image: url(:/image/logo.png);"))
        self.frame_top_logo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_top_logo.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_top_logo.setObjectName(_fromUtf8("frame_top_logo"))

        # 顶部名称文字
        self.frame_top_name = QtGui.QFrame(self.frame_top)
        self.frame_top_name.setGeometry(QtCore.QRect(210, 20, 360, 80))
        self.frame_top_name.setStyleSheet(_fromUtf8("border-image: url(:/image/top_name.png);"))
        self.frame_top_name.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_top_name.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_top_name.setObjectName(_fromUtf8("frame_top_name"))

        # 底部背景
        self.frame_bottom = QtGui.QFrame(self.frame_bkground)
        self.frame_bottom.setGeometry(QtCore.QRect(0, 479, 751, 31))
        self.frame_bottom.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_blue.jpg);"))
        self.frame_bottom.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_bottom.setObjectName(_fromUtf8("frame_bottom"))
        self.label_bottom_version = QtGui.QLabel(self.frame_bottom)
        self.label_bottom_version.setGeometry(QtCore.QRect(600, 0, 151, 31))

        # 文字
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        # 底部 版本
        self.label_bottom_version.setFont(font)
        self.label_bottom_version.setStyleSheet(_fromUtf8(""))
        self.label_bottom_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bottom_version.setObjectName(_fromUtf8("label_bottom_version"))
        self.listWidget_left = QtGui.QListWidget(self.frame_bkground)
        self.listWidget_left.setGeometry(QtCore.QRect(0, 111, 111, 368))

        # 中间左边 列表
        self.listWidget_left.setFont(font)
        self.listWidget_left.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_grey.jpg);"))
        self.listWidget_left.setObjectName(_fromUtf8("listWidget_left"))

        # 中间右边
        self.frame_mid_right = QtGui.QStackedWidget(self.frame_bkground)
        self.frame_mid_right.setGeometry(QtCore.QRect(110, 111, 640, 368))
        self.frame_mid_right.setStyleSheet(_fromUtf8("border-image: url(:/image/bkg_white.jpg);"))
        self.frame_mid_right.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_mid_right.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_mid_right.setObjectName(_fromUtf8("frame_mid_right"))

import image_rc
