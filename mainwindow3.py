# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\qt\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1062, 640)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.Screen = QtWidgets.QLabel(self.centralWidget)
        self.Screen.setGeometry(QtCore.QRect(290, 55, 755, 491))
        self.Screen.setAutoFillBackground(False)
        self.Screen.setObjectName("Screen")
        self.Title = QtWidgets.QTextEdit(self.centralWidget)
        self.Title.setGeometry(QtCore.QRect(180, 10, 960, 50))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        self.Title.setFont(font)
        self.Title.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:none")
        self.Title.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Title.setReadOnly(True)
        self.Title.setObjectName("Title")
        self.BorderLeft = QtWidgets.QLabel(self.centralWidget)
        self.BorderLeft.setGeometry(QtCore.QRect(285, 50, 5, 500))
        self.BorderLeft.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BorderLeft.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.422886 rgba(47, 48, 50, 255));")
        self.BorderLeft.setObjectName("BorderLeft")
        self.BorderRight = QtWidgets.QLabel(self.centralWidget)
        self.BorderRight.setGeometry(QtCore.QRect(1045, 50, 5, 500))
        self.BorderRight.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.422886 rgba(47, 48, 50, 255));")
        self.BorderRight.setObjectName("BorderRight")
        self.BorderBottom = QtWidgets.QLabel(self.centralWidget)
        self.BorderBottom.setGeometry(QtCore.QRect(285, 545, 765, 5))
        self.BorderBottom.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.422886 rgba(47, 48, 50, 255));")
        self.BorderBottom.setObjectName("BorderBottom")
        self.ChooseProbe = QtWidgets.QPushButton(self.centralWidget)
        self.ChooseProbe.setGeometry(QtCore.QRect(30, 20, 100, 30))
        self.ChooseProbe.setObjectName("ChooseProbe")
        self.Probe = QtWidgets.QLabel(self.centralWidget)
        self.Probe.setGeometry(QtCore.QRect(30, 90, 100, 200))
        self.Probe.setObjectName("Probe")
        self.ScreenShot = QtWidgets.QPushButton(self.centralWidget)
        self.ScreenShot.setGeometry(QtCore.QRect(150, 20, 100, 30))
        self.ScreenShot.setObjectName("ScreenShot")
        self.BorderBottom_2 = QtWidgets.QLabel(self.centralWidget)
        self.BorderBottom_2.setGeometry(QtCore.QRect(285, 50, 765, 5))
        self.BorderBottom_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.422886 rgba(47, 48, 50, 255));")
        self.BorderBottom_2.setObjectName("BorderBottom_2")
        self.Probe_2 = QtWidgets.QLabel(self.centralWidget)
        self.Probe_2.setGeometry(QtCore.QRect(150, 90, 100, 200))
        self.Probe_2.setObjectName("Probe_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(55, 310, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(174, 310, 54, 12))
        self.label_2.setObjectName("label_2")
        self.CamName = QtWidgets.QLabel(self.centralWidget)
        self.CamName.setGeometry(QtCore.QRect(590, 570, 201, 31))
        self.CamName.setObjectName("CamName")
        self.playBtn = QtWidgets.QPushButton(self.centralWidget)
        self.playBtn.setGeometry(QtCore.QRect(960, 580, 75, 23))
        self.playBtn.setObjectName("playBtn")
        self.camList = QtWidgets.QListWidget(self.centralWidget)
        self.camList.setGeometry(QtCore.QRect(10, 381, 261, 241))
        self.camList.setObjectName("camList")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(20, 360, 54, 12))
        self.label_4.setObjectName("label_4")
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
        self.ScreenShot.setText(_translate("MainWindow", "视频截图"))
        self.BorderBottom_2.setText(_translate("MainWindow", "TextLabel"))
        self.Probe_2.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "目标人物"))
        self.label_2.setText(_translate("MainWindow", "匹配结果"))
        self.CamName.setText(_translate("MainWindow", "TextLabel"))
        self.playBtn.setText(_translate("MainWindow", "播放"))
        self.label_4.setText(_translate("MainWindow", "相机列表"))

