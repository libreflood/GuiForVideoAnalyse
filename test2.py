#!/usr/bin/python3  
# -*- coding: utf-8 -*-  
  
"""  
ZetCode PyQt5 tutorial   
  
In the example, we draw randomly 1000 red points   
on the window.  
  
author: Jan Bodnar  
website: zetcode.com   
last edited: January 2015  
"""  
  
import sys, random  
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *  
  
  
class Example(QtWidgets.QWidget):  
      
    def __init__(self):  
        super().__init__()  
          
        self.initUI()  
          
          
    def initUI(self):        
  
        self.setGeometry(300, 300, 280, 170)  
        self.setWindowTitle('Points')  
        self.show()  
          
  
    def paintEvent(self, e):  
  
        qp = QtGui.QPainter()  
        qp.begin(self)  
        self.drawPoints(qp)  
        qp.end()  
          
          
    def drawPoints(self, qp):  
        
        qp.setPen(QtCore.Qt.red)  
        size = self.size()  
          
        qp.drawRect(10,10,30,30)
        for i in range(1000):  
            x = random.randint(1, size.width()-1)  
            y = random.randint(1, size.height()-1)  
            qp.drawPoint(x, y)       
                  
          
if __name__ == '__main__':  
      
    app = QtWidgets.QApplication(sys.argv)  
    ex = Example()  
    sys.exit(app.exec_())  