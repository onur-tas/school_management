# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/onur/Documents/GitHub/school-management-system/sign/main_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QtCore.QSize(600, 500))
        MainWindow.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(600, 500))
        self.frame.setMaximumSize(QtCore.QSize(600, 500))
        self.frame.setSizeIncrement(QtCore.QSize(600, 500))
        self.frame.setStyleSheet("\n"
"background-image: url(sign/assets/back2.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(100, 100, 321, 341))
        self.frame_2.setStyleSheet("background-image: url(:/newPrefix/C:/Users/MainUser/Desktop/tech_groupproject/school-management-system/sign/assets/back2.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.login_Button = QtWidgets.QPushButton(self.frame_2)
        self.login_Button.setGeometry(QtCore.QRect(50, 230, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login_Button.setFont(font)
        self.login_Button.setStyleSheet("background-color: rgb(249, 186, 50);")
        self.login_Button.setObjectName("login_Button")
        self.signup_Button = QtWidgets.QPushButton(self.frame_2)
        self.signup_Button.setGeometry(QtCore.QRect(180, 230, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signup_Button.setFont(font)
        self.signup_Button.setStyleSheet("background-color: rgb(249, 186, 50);")
        self.signup_Button.setObjectName("signup_Button")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_Button.setText(_translate("MainWindow", "LOGIN"))
        self.signup_Button.setText(_translate("MainWindow", "SIGNUP"))
#import b_rc