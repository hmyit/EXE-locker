# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Sun Apr 24 23:56:06 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(423, 653)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainDialog.sizePolicy().hasHeightForWidth())
        MainDialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainDialog.setWindowIcon(icon)
        self.frame = QtGui.QFrame(MainDialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 431, 91))
        self.frame.setMinimumSize(QtCore.QSize(421, 0))
        self.frame.setStyleSheet("background-color: rgb(33, 150, 243);")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 43, 58))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/lock.png"))
        self.label.setObjectName("label")
        self.fontLabel = QtGui.QLabel(self.frame)
        self.fontLabel.setGeometry(QtCore.QRect(70, 20, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        font.setWeight(75)
        font.setBold(True)
        self.fontLabel.setFont(font)
        self.fontLabel.setStyleSheet("#fontLabel {\n"
"    color: white;\n"
"}")
        self.fontLabel.setObjectName("fontLabel")
        self.step1GroupBox = QtGui.QGroupBox(MainDialog)
        self.step1GroupBox.setGeometry(QtCore.QRect(20, 110, 381, 91))
        self.step1GroupBox.setStyleSheet("QGroupBox::title {\n"
"    font-size: 32px;\n"
"}")
        self.step1GroupBox.setFlat(False)
        self.step1GroupBox.setObjectName("step1GroupBox")
        self.locationLineEdit = QtGui.QLineEdit(self.step1GroupBox)
        self.locationLineEdit.setEnabled(True)
        self.locationLineEdit.setGeometry(QtCore.QRect(20, 40, 251, 31))
        self.locationLineEdit.setReadOnly(True)
        self.locationLineEdit.setObjectName("locationLineEdit")
        self.pickFileButton = QtGui.QPushButton(self.step1GroupBox)
        self.pickFileButton.setGeometry(QtCore.QRect(280, 40, 91, 31))
        self.pickFileButton.setObjectName("pickFileButton")
        self.lockButton = QtGui.QPushButton(MainDialog)
        self.lockButton.setEnabled(True)
        self.lockButton.setGeometry(QtCore.QRect(300, 600, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lockButton.setFont(font)
        self.lockButton.setStyleSheet("#lockButton {\n"
"    border: 2px solid #1976D2;\n"
"    background-color: #2196f3;\n"
"    min-width: 80px;\n"
"    color: white;\n"
"}\n"
"#lockButton:hover {\n"
"    background-color: #42A5F5;\n"
"    \n"
"}\n"
"\n"
"#lockButton:pressed {\n"
"    background-color: #0D47A1;\n"
"}\n"
"\n"
"#lockButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"#lockButton:default {\n"
"    border-color: white; /* make the default button prominent */\n"
"}\n"
"\n"
"#lockButton:disabled {\n"
"    background-color: #E3F2FD;\n"
"    border-color: #BBDEFB;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lockButton.setIcon(icon1)
        self.lockButton.setFlat(False)
        self.lockButton.setObjectName("lockButton")
        self.groupBox = QtGui.QGroupBox(MainDialog)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(20, 220, 381, 361))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    font-size: 24px;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.stackedWidget = QtGui.QStackedWidget(self.groupBox)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 30, 351, 271))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.passwordLineEdit = QtGui.QLineEdit(self.page)
        self.passwordLineEdit.setGeometry(QtCore.QRect(20, 30, 261, 31))
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordAgainLineEdit = QtGui.QLineEdit(self.page)
        self.passwordAgainLineEdit.setGeometry(QtCore.QRect(20, 100, 261, 31))
        self.passwordAgainLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordAgainLineEdit.setObjectName("passwordAgainLineEdit")
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label_2.setStyleSheet("font: 75 10pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 131, 16))
        self.label_3.setStyleSheet("font: 75 10pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 271, 31))
        self.label_4.setStyleSheet("color: red;\n"
"font-size: 14px;")
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.page_2)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 70, 271, 31))
        self.dateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 15), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_5 = QtGui.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 321, 41))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_2)
        self.frame_2 = QtGui.QFrame(self.groupBox)
        self.frame_2.setGeometry(QtCore.QRect(30, 240, 321, 61))
        self.frame_2.setStyleSheet("background-color: rgba(66, 165, 245, 0.1);")
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.warningLabel = QtGui.QLabel(self.frame_2)
        self.warningLabel.setGeometry(QtCore.QRect(10, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.warningLabel.setFont(font)
        self.warningLabel.setStyleSheet("#warningLabel {\n"
"    font-size: 16px;\n"
"}")
        self.warningLabel.setWordWrap(True)
        self.warningLabel.setObjectName("warningLabel")
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(30, 330, 361, 17))
        self.checkBox.setObjectName("checkBox")
        self.label_6 = QtGui.QLabel(MainDialog)
        self.label_6.setGeometry(QtCore.QRect(20, 600, 151, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/images/iceapps_logo.png"))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(MainDialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QtGui.QApplication.translate("MainDialog", "EXE Locker", None, QtGui.QApplication.UnicodeUTF8))
        self.fontLabel.setText(QtGui.QApplication.translate("MainDialog", "EXE Locker", None, QtGui.QApplication.UnicodeUTF8))
        self.step1GroupBox.setTitle(QtGui.QApplication.translate("MainDialog", "Select EXE to lock", None, QtGui.QApplication.UnicodeUTF8))
        self.pickFileButton.setText(QtGui.QApplication.translate("MainDialog", "Pick EXE File", None, QtGui.QApplication.UnicodeUTF8))
        self.lockButton.setText(QtGui.QApplication.translate("MainDialog", "Lock EXE", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainDialog", "Lock Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainDialog", "Enter Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainDialog", "Enter Password again", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainDialog", "Password and Password again must match.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainDialog", "Select the time and date after which file will be unlocked on opening.", None, QtGui.QApplication.UnicodeUTF8))
        self.warningLabel.setText(QtGui.QApplication.translate("MainDialog", "Remember, if you lose the password, you lose the file.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainDialog", "Make a backup of the exe as .exe.old file (Check for testing)", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
