# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/onur/Documents/GitHub/school-management-system/sign/main_3.ui'
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
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QtCore.QSize(600, 500))
        self.frame.setMaximumSize(QtCore.QSize(600, 500))
        self.frame.setSizeIncrement(QtCore.QSize(600, 500))
        self.frame.setStyleSheet("background-color: rgb(10, 98, 38);\n"
"background-image: url(:/newPrefix/back2.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.email_label = QtWidgets.QLabel(self.frame)
        self.email_label.setGeometry(QtCore.QRect(80, 180, 150, 30))
        self.email_label.setMinimumSize(QtCore.QSize(150, 30))
        self.email_label.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("background-color: rgb(249, 186, 50);\n"
"border-color: rgb(0, 0, 0);")
        self.email_label.setObjectName("email_label")
        self.password_label = QtWidgets.QLabel(self.frame)
        self.password_label.setGeometry(QtCore.QRect(80, 260, 150, 30))
        self.password_label.setMinimumSize(QtCore.QSize(150, 30))
        self.password_label.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("background-color: rgb(249, 186, 50);\n"
"border-color: rgb(0, 0, 0);")
        self.password_label.setObjectName("password_label")
        self.email = QtWidgets.QLineEdit(self.frame)
        self.email.setGeometry(QtCore.QRect(250, 180, 250, 30))
        self.email.setMinimumSize(QtCore.QSize(250, 30))
        self.email.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: rgb(249, 186, 50);")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(250, 260, 250, 30))
        self.password.setMinimumSize(QtCore.QSize(250, 30))
        self.password.setMaximumSize(QtCore.QSize(250, 30))
        self.password.setStyleSheet("background-color: rgb(249, 186, 50);\n"
"border-color: rgb(0, 0, 0);")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(400, 330, 100, 50))
        self.pushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(249, 186, 50);")
        self.pushButton.setObjectName("pushButton")
        self.email.raise_()
        self.email_label.raise_()
        self.password_label.raise_()
        self.password.raise_()
        self.pushButton.raise_()
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.email_label.setText(_translate("MainWindow", "E-mail"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
