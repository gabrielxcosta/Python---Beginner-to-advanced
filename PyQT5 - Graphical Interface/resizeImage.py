# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resizeImage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(596, 485)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.inputWidth = QtWidgets.QLineEdit(self.centralwidget)
        self.inputWidth.setObjectName("inputWidth")
        self.gridLayout.addWidget(self.inputWidth, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 2, 1, 1)
        self.inputHeight = QtWidgets.QLineEdit(self.centralwidget)
        self.inputHeight.setObjectName("inputHeight")
        self.gridLayout.addWidget(self.inputHeight, 3, 3, 1, 1)
        self.btnResize = QtWidgets.QPushButton(self.centralwidget)
        self.btnResize.setObjectName("btnResize")
        self.gridLayout.addWidget(self.btnResize, 3, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setObjectName("btnSave")
        self.gridLayout.addWidget(self.btnSave, 4, 4, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 576, 378))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.imageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.gridLayout_2.addWidget(self.imageLabel, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 2, 5)
        self.chooseFile = QtWidgets.QPushButton(self.centralwidget)
        self.chooseFile.setObjectName("chooseFile")
        self.gridLayout.addWidget(self.chooseFile, 2, 4, 1, 1)
        self.inputOpenFile = QtWidgets.QLineEdit(self.centralwidget)
        self.inputOpenFile.setObjectName("inputOpenFile")
        self.gridLayout.addWidget(self.inputOpenFile, 2, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resize image"))
        self.label_2.setText(_translate("MainWindow", "Height"))
        self.btnResize.setText(_translate("MainWindow", "Resize"))
        self.label.setText(_translate("MainWindow", "Width"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.chooseFile.setText(_translate("MainWindow", "Choose file"))