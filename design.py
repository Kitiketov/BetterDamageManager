# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(466, 274)
        MainWindow.setStyleSheet("\n"
"TitleBar {\n"
"    background-color: #2a3440;\n"
"}")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background-color: rgb(59, 59, 59);\n"
"    color: rgb(185, 187, 190);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(8, 6, 451, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(59, 59, 59);\n"
"    color: rgb(185, 187, 190);\n"
"    font: 10pt \"Terminal\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(97, 97, 97);\n"
"    color: rgb(216, 217, 218);\n"
"    font: 10pt \"Terminal\";\n"
"}")
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_2.addWidget(self.startButton)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color: rgb(0, 153, 0);\n"
"border-radius: 5px\n"
"}\n"
"QLabel:disabled{\n"
"     background-color:rgba(59, 59,59,255);\n"
"    color: rgba(216, 217, 218,100);\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comBox.sizePolicy().hasHeightForWidth())
        self.comBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comBox.setFont(font)
        self.comBox.setStyleSheet("QComboBox{\n"
"    background-color: rgb(59, 59, 59);\n"
"    color: rgb(185, 187, 190);\n"
"    font: 10pt \"Terminal\";\n"
"}\n"
"QComboBox:hover{\n"
"    background-color:rgb(97, 97, 97);\n"
"    color: rgb(216, 217, 218);\n"
"    font: 10pt \"Terminal\";\n"
"}\n"
"QComboBox:disabled{\n"
"    background-color:rgb(40, 40, 40);\n"
"    color: rgb(216, 217, 218);\n"
"    font: 10pt \"Terminal\";\n"
"}\n"
"")
        self.comBox.setObjectName("comBox")
        self.horizontalLayout_4.addWidget(self.comBox)
        self.openPortButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openPortButton.sizePolicy().hasHeightForWidth())
        self.openPortButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.openPortButton.setFont(font)
        self.openPortButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(59, 59, 59);\n"
"    color: rgb(185, 187, 190);\n"
"    font: 10pt \"Terminal\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(97, 97, 97);\n"
"    color: rgb(216, 217, 218);\n"
"    font: 10pt \"Terminal\";\n"
"}")
        self.openPortButton.setObjectName("openPortButton")
        self.horizontalLayout_4.addWidget(self.openPortButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.vibroTestButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.vibroTestButton.setFont(font)
        self.vibroTestButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(59, 59, 59);\n"
"    color: rgb(185, 187, 190);\n"
"    font: 10pt \"Terminal\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(97, 97, 97);\n"
"    color: rgb(216, 217, 218);\n"
"    font: 10pt \"Terminal\";\n"
"}")
        self.vibroTestButton.setObjectName("vibroTestButton")
        self.horizontalLayout_5.addWidget(self.vibroTestButton)
        self.shockTestButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.shockTestButton.setFont(font)
        self.shockTestButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(59, 59, 59);\n"
"    color: rgb(185, 187, 190);\n"
"    font: 10pt \"Terminal\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(97, 97, 97);\n"
"    color: rgb(216, 217, 218);\n"
"    font: 10pt \"Terminal\";\n"
"}")
        self.shockTestButton.setObjectName("shockTestButton")
        self.horizontalLayout_5.addWidget(self.shockTestButton)
        self.powerUpButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerUpButton.sizePolicy().hasHeightForWidth())
        self.powerUpButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.powerUpButton.setFont(font)
        self.powerUpButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(59, 59, 59);\n"
"    color: rgb(185, 187, 190);\n"
"    font: 10pt \"Terminal\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(97, 97, 97);\n"
"    color: rgb(216, 217, 218);\n"
"    font: 10pt \"Terminal\";\n"
"}")
        self.powerUpButton.setObjectName("powerUpButton")
        self.horizontalLayout_5.addWidget(self.powerUpButton)
        self.powerDownButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerDownButton.sizePolicy().hasHeightForWidth())
        self.powerDownButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.powerDownButton.setFont(font)
        self.powerDownButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(59, 59, 59);\n"
"    color: rgb(185, 187, 190);\n"
"    font: 10pt \"Terminal\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(97, 97, 97);\n"
"    color: rgb(216, 217, 218);\n"
"    font: 10pt \"Terminal\";\n"
"}")
        self.powerDownButton.setObjectName("powerDownButton")
        self.horizontalLayout_5.addWidget(self.powerDownButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editFolderPath = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.editFolderPath.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editFolderPath.sizePolicy().hasHeightForWidth())
        self.editFolderPath.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editFolderPath.setFont(font)
        self.editFolderPath.setStyleSheet("QPushButton{\n"
"    background-color: rgb(59, 59, 59);\n"
"    color: rgb(185, 187, 190);\n"
"    font: 10pt \"Terminal\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(97, 97, 97);\n"
"    color: rgb(216, 217, 218);\n"
"    font: 10pt \"Terminal\";\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color:rgb(40, 40, 40);\n"
"    color: rgb(216, 217, 218);\n"
"    font: 10pt \"Terminal\";\n"
"}")
        self.editFolderPath.setObjectName("editFolderPath")
        self.horizontalLayout.addWidget(self.editFolderPath)
        self.folderPath = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(1)
        self.folderPath.setFont(font)
        self.folderPath.setText("")
        self.folderPath.setObjectName("folderPath")
        self.horizontalLayout.addWidget(self.folderPath)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.console = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.console.setStyleSheet("QTextEdit{\n"
"background-color:rgb(97, 97,97);\n"
"}\n"
"QScrollBar:vertical {\n"
"    background:rgb(60, 64, 71);\n"
"    width:10px;\n"
"    border: none;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    border: 1px solid rgb(255, 255, 0);\n"
"    background:rgb(185, 187, 190);\n"
"    border: none;\n"
"    \n"
"}")
        self.console.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.console.setReadOnly(True)
        self.console.setObjectName("console")
        self.verticalLayout.addWidget(self.console)
        self.errorMessage = QtWidgets.QLabel(self.centralwidget)
        self.errorMessage.setEnabled(False)
        self.errorMessage.setGeometry(QtCore.QRect(11, 220, 431, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorMessage.sizePolicy().hasHeightForWidth())
        self.errorMessage.setSizePolicy(sizePolicy)
        self.errorMessage.setStyleSheet("QLabel{\n"
"    \n"
"    border-radius: 10px;\n"
"    background-color:rgb(236, 66, 69);\n"
"    color: rgb(216, 217, 218);\n"
"    padding-left: auto;\n"
"    padding-right: auto;\n"
"    font: 8pt \"Terminal\";\n"
"    \n"
"}\n"
"QLabel:disabled{\n"
"     background-color:rgba(0, 0, 0, 0);\n"
"    color: rgba(216, 217, 218,0);\n"
"}")
        self.errorMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.errorMessage.setObjectName("errorMessage")
        self.counterDmgLabel = QtWidgets.QLabel(self.centralwidget)
        self.counterDmgLabel.setGeometry(QtCore.QRect(400, 245, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(5)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.counterDmgLabel.setFont(font)
        self.counterDmgLabel.setStyleSheet("QLabel{\n"
"background-color : rbga(0,0,0,0);\n"
"}\n"
"")
        self.counterDmgLabel.setObjectName("counterDmgLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Start tracking"))
        self.label.setText(_translate("MainWindow", "Offline"))
        self.openPortButton.setText(_translate("MainWindow", "Open Port"))
        self.label_2.setText(_translate("MainWindow", "Test"))
        self.vibroTestButton.setText(_translate("MainWindow", "Vibro"))
        self.shockTestButton.setText(_translate("MainWindow", "Shock"))
        self.powerUpButton.setText(_translate("MainWindow", "+"))
        self.powerDownButton.setText(_translate("MainWindow", "-"))
        self.editFolderPath.setText(_translate("MainWindow", "Edit Folder"))
        self.errorMessage.setText(_translate("MainWindow", "Error"))
        self.counterDmgLabel.setText(_translate("MainWindow", "0"))
