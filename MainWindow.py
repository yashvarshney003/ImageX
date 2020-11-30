# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageX_desktop.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from scipy import ndimage, misc
import os
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QLineEdit, QFileDialog, QHBoxLayout, QLabel, QTextEdit
from PyQt5.QtGui import QIcon, QPixmap  
import webbrowser
from srgan import train, sample_images


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 387)
        self.fileName = ''
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 426, 354))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_2.setEnabled(True)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 6, 10, 6)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(460, 20, 371, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(490, 60, 400, 271))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.initUI()


    def initUI(self):
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_3.clicked.connect(self.openIssueLink)
        self.radioButton.clicked.connect(self.options_1)
        self.radioButton_2.clicked.connect(self.options_4)
        self.radioButton_3.clicked.connect(self.options_3)
        self.radioButton_4.clicked.connect(self.options_2)

        self.show()

    def options_1(self):
        self.textBrowser_2.setText("You selected Image Super Resolution")
        self.pushButton_2.clicked.connect(self.openFileNameDialog)

    def options_2(self):
        self.textBrowser_2.setText("You selected Image Object Detection")    

    def options_3(self):
        self.textBrowser_2.setText("You selected Image Compression")
    
    def options_4(self):
        self.textBrowser_2.setText("You selected Image Fusion - Multifocus")

    def showImg(self, ):
        hbox = QHBoxLayout(self)                                                                                                           
        pixmap = QPixmap(self.fileName)                                                                                                        

        lbl = QLabel(self)                                                                                                                 
        lbl.setPixmap(pixmap)                                                                                                              

        hbox.addWidget(lbl)                                                                                                                
        self.setLayout(hbox)                                                                                                               

        self.move(300, 200)                                                                                                                
        self.setWindowTitle('Image with PyQt')                                                                                             
        self.show() 

    @pyqtSlot()
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Select file to insert", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            print(self.fileName)
            self.label.setText("Attached image: "+self.fileName)
            pixmap = QPixmap(self.fileName)
            pixmap2 = pixmap.scaledToWidth(100)
            pixmap3 = pixmap.scaledToHeight(400)
            self.label_2.setPixmap(pixmap3)
            #testing 
            sample_images(1000)
            self.showImg()



        
    @pyqtSlot()
    def openIssueLink(self):
        webbrowser.open('https://github.com/robustTechie/SRGAN/issues/new', new=2)                  
        

    @pyqtSlot()
    def on_click(self):
        sys.exit()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Medium Italic\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Welcome to ImageX</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">An Open Source Imaging client of </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">pyImageX library</span></p></body></html>"))
        self.radioButton.setText(_translate("Dialog", "Image Super Resolution"))
        self.radioButton_4.setText(_translate("Dialog", "Object Detection"))
        self.radioButton_3.setText(_translate("Dialog", "Image compression"))
        self.radioButton_2.setText(_translate("Dialog", "Image Fusion - Multi focus"))
        self.pushButton_2.setText(_translate("Dialog", "Insert"))
        self.pushButton_3.setText(_translate("Dialog", "Report an issue"))
        self.pushButton.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "Attached Image: "))
        self.label_2.setText(_translate("Dialog", "No Image"))

