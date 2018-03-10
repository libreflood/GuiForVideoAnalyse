import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainwindow3 import Ui_MainWindow
from PIL import ImageQt
from PIL import Image
import io

class MyForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Screen = MyScreen(self.ui.centralWidget)
        self.ui.Screen.setGeometry(QtCore.QRect(290, 55, 755, 491))
        # self.ui.Screen.setAutoFillBackground(False)
        self.ui.Screen.setObjectName("Screen")
        self.ui.ChooseProbe.clicked.connect(self.openFile)
        self.ui.Screen.oksignal.connect(lambda: self.bbb())

    #Description: 单击按钮，弹出对话框，选择probe图片，并在按钮下方显示图片
    def openFile(self):
        self.probeImgDir = QtWidgets.QFileDialog.getOpenFileName(self, "Open", "d://", "")
        self.probeImg = QtGui.QPixmap(self.probeImgDir[0])
        self.probeImg = self.probeImg.scaled(self.ui.Probe.size(), QtCore.Qt.IgnoreAspectRatio)
        self.ui.Probe.setPixmap(self.probeImg)
        tmpPixmap = self.ui.Probe.pixmap()
        self.showInScreen(tmpPixmap)

    #Description: 将图片显示到屏幕上
    #Args：
    #       Img 待显示的图片
    def showInScreen(self, Img):
        Img.save("hhh.jpg")
        Img = Img.scaled(self.ui.Screen.size(), QtCore.Qt.IgnoreAspectRatio)
        self.ui.Screen.setPixmap(Img)
        #self.ui.Screen.update()

    #Description：槽函数，用于测试
    def bbb (self):
        print ("bbb")
        self.probeImg = QtGui.QPixmap("aaa.jpg")
        self.probeImg = self.probeImg.scaled(self.ui.Probe.size(), QtCore.Qt.IgnoreAspectRatio)
        self.ui.Probe.setPixmap(self.probeImg)


class MyScreen(QtWidgets.QLabel):
    oksignal = pyqtSignal()
    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        #super().__init__()
        self.setMouseTracking(False)
        self.first_x, self.first_y = -1, -1 #绘制矩形框的初始点
        '''self.probeImg = QtGui.QPixmap("aaa.jpg")
        self.probeImg = self.probeImg.scaled(self.size(), QtCore.Qt.IgnoreAspectRatio)
        self.setPixmap(self.probeImg)'''
    #Description：绘制矩形框。这是事件函数，无需调用
    def paintEvent(self, event):
        QLabel.paintEvent(self,event)
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)

        if self.first_x != -1 and self.first_y != -1:
            painter.drawRect(self.first_x, self.first_y, self.pos_x - self.first_x, self.pos_y - self.first_y)
            #print (self.first_x, self.first_y, self.pos_x, self.pos_y)
        painter.end()

    def mouseMoveEvent(self, event):
        '''
        按住鼠标移动事件：更新pos_x和pos_y的值
        调用update()函数在这里相当于调用paintEvent()函数
        每次update()时，之前调用的paintEvent()留下的痕迹都会清空
        '''
        self.pos_x = event.pos().x()
        self.pos_y = event.pos().y()
        self.update()

    def mousePressEvent(self, event):
        self.first_x = event.pos().x()
        self.first_y = event.pos().y()

    def mouseReleaseEvent(self, event):
        selectPerson = self.pixmap().copy(self.first_x, self.first_y, event.pos().x() - self.first_x, event.pos().y() - self.first_y)
        selectPerson.save("aaa.jpg")
        self.first_x, self.first_y = -1, -1
        self.update()
        self.oksignal.emit()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


