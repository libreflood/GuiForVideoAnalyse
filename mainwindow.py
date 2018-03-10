# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost! xuyue: why?

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 685)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.Screen = QtWidgets.QLabel(self.centralWidget)
        self.Screen.setGeometry(QtCore.QRect(280, 50, 680, 425))
        self.Screen.setAutoFillBackground(False)
        self.Screen.setObjectName("Screen")
        self.ResultList = QtWidgets.QListWidget(self.centralWidget)
        self.ResultList.setGeometry(QtCore.QRect(280, 475, 671, 200))
        self.ResultList.setStyleSheet("background-color:transparent;\n"
"border:none")
        self.ResultList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ResultList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ResultList.setAutoScrollMargin(0)
        self.ResultList.setIconSize(QtCore.QSize(90, 90))
        self.ResultList.setTextElideMode(QtCore.Qt.ElideNone)
        self.ResultList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.ResultList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ResultList.setMovement(QtWidgets.QListView.Static)
        self.ResultList.setProperty("isWrapping", False)
        self.ResultList.setResizeMode(QtWidgets.QListView.Adjust)
        self.ResultList.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.ResultList.setGridSize(QtCore.QSize(115, 115))
        self.ResultList.setViewMode(QtWidgets.QListView.IconMode)
        self.ResultList.setBatchSize(6)
        self.ResultList.setObjectName("ResultList")
        self.Title = QtWidgets.QTextEdit(self.centralWidget)
        self.Title.setGeometry(QtCore.QRect(0, 0, 960, 50))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        self.Title.setFont(font)
        self.Title.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:none")
        self.Title.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Title.setReadOnly(True)
        self.Title.setObjectName("Title")
        self.BorderLeft = QtWidgets.QLabel(self.centralWidget)
        self.BorderLeft.setGeometry(QtCore.QRect(0, 0, 10, 685))
        self.BorderLeft.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BorderLeft.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.422886 rgba(47, 48, 50, 255));")
        self.BorderLeft.setObjectName("BorderLeft")
        self.BorderRight = QtWidgets.QLabel(self.centralWidget)
        self.BorderRight.setGeometry(QtCore.QRect(950, 0, 10, 685))
        self.BorderRight.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.422886 rgba(47, 48, 50, 255));")
        self.BorderRight.setObjectName("BorderRight")
        self.BorderBottom = QtWidgets.QLabel(self.centralWidget)
        self.BorderBottom.setGeometry(QtCore.QRect(0, 675, 960, 10))
        self.BorderBottom.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.422886 rgba(47, 48, 50, 255));")
        self.BorderBottom.setObjectName("BorderBottom")
        self.ChooseProbe = QtWidgets.QPushButton(self.centralWidget)
        self.ChooseProbe.setGeometry(QtCore.QRect(60, 10, 120, 50))
        self.ChooseProbe.setObjectName("ChooseProbe")
        self.Probe = QtWidgets.QLabel(self.centralWidget)
        self.Probe.setGeometry(QtCore.QRect(70, 80, 100, 200))
        self.Probe.setObjectName("Probe")
        self.VideoList = QtWidgets.QTextEdit(self.centralWidget)
        self.VideoList.setGeometry(QtCore.QRect(10, 300, 270, 375))
        self.VideoList.setObjectName("VideoList")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸比对系统"))
        self.Screen.setText(_translate("MainWindow", "TextLabel"))
        self.Title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Mono\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">行人重识别系统</span></p></body></html>"))
        self.BorderLeft.setText(_translate("MainWindow", "TextLabel"))
        self.BorderRight.setText(_translate("MainWindow", "TextLabel"))
        self.BorderBottom.setText(_translate("MainWindow", "TextLabel"))
        self.ChooseProbe.setText(_translate("MainWindow", "选择图片"))
        self.Probe.setText(_translate("MainWindow", "TextLabel"))

