# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sudokuqt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel)
import sys
class window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sudoku solver")
        self.top=100
        self.left=100
        self.width=680
        self.height=500
        self.setGeometry(self.top, self.left, self.width, self.height)
      
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 1121, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 470, 161, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonaction)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        self.pushButton.setText(_translate("MainWindow", "Find the solution"))
    def buttonaction(self,MainWindow):
        for i in range(9):
             for j in range(9):
                 try:
                     item1=self.tableWidget.item(i,j)
                     a[i][j]=int(item1.text())
                 except:
                     a[i][j]=0
            
        c=[1,2,3,4,5,6,7,8,9]
        for u in range(30):
            arr=[]
            b=[]
            list1=[]
            list2=[]
            fit(a,c,b,arr,list1,list2)
        print(a)
        print("\n")
        backtrack(a,arr,0,list1,list2)

        print(a)
        self.w=window2()
        self.w.show()
        self.hide()
         
 
def check(a,nu,b,i1,j1):
    
    for ik in range(9):
        if a[i1][ik]==nu:
            return
    for ik in range(9):
        if a[ik][j1]==nu:
            return
        
    le=i1//3
    lu=j1//3
    for ik in range(int(le*3),int(le*3+3)):
        for ver in range(int(lu*3),int(lu*3+3)):
            if a[ik][ver]==nu:
                return 
                
    b.append(nu)



def check_2(a,i1,j1,nu):
    for ik in range(9):
        if a[i1][ik]==nu:
            return 0
    for ik in range(9):
        if a[ik][j1]==nu:
            return 0
    le=i1//3
    lu=j1//3
    for ik in range(int(le*3),int(le*3+3)):
        for ver in range(int(lu*3),int(lu*3+3)):
            if a[ik][ver]==nu:
                return 0
                
    return 1            
                
            
                     
    
def backtrack(a,arr,k,list1,list2):
    if k==len(arr):
        print("yes")
        for ui in a:
            print(ui)
        sys.exit()
    i5=list1[k]
    j5=list2[k]
   
    
    for iu in arr[k]:
       
            
        z=check_2(a,i5,j5,iu)
        
        
        if z==1:
            a[i5][j5]=iu
            backtrack(a,arr,k+1,list1,list2)
    a[i5][j5]=0
            
    

                
    
def fit(a,c,b,arr,list1,list2):
    for i1 in range(9):
        for j2 in range(9):
            if a[i1][j2]==0:
                list1.append(i1)
                list2.append(j2)
                for num in c:
                    check(a,num,b,i1,j2)
                if len(b)==1:
                    a[i1][j2]=b[0]
                    list1.remove(i1)
                    list2.remove(j2)
                else:
                    arr.append(b)
                b=[]
          
if __name__ == "__main__":
    
    a=[
       [-1,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0]]
    arr=[]
    list1=[]
    list2=[]
    b=[]
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
  
    sys.exit(app.exec_())
    
   
    
