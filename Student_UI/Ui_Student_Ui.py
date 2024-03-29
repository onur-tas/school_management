# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\MainUser\Documents\GitHub\Sema\school_update\Student_UI\Student_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Student_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 800)
        MainWindow.setMinimumSize(QtCore.QSize(960, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1150, 800))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(270, 10, 861, 771))
        self.tabWidget.setMinimumSize(QtCore.QSize(861, 771))
        self.tabWidget.setMaximumSize(QtCore.QSize(1150, 800))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(57, 57, 57);")
        self.tabWidget.setObjectName("tabWidget")
        self.student_main = QtWidgets.QWidget()
        self.student_main.setObjectName("student_main")
        self.student_main_date = QtWidgets.QLabel(self.student_main)
        self.student_main_date.setGeometry(QtCore.QRect(20, 40, 250, 50))
        self.student_main_date.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.student_main_date.setFont(font)
        self.student_main_date.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.student_main_date.setObjectName("student_main_date")
        self.label_main_announcements = QtWidgets.QLabel(self.student_main)
        self.label_main_announcements.setGeometry(QtCore.QRect(20, 160, 271, 40))
        self.label_main_announcements.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_main_announcements.setFont(font)
        self.label_main_announcements.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_main_announcements.setObjectName("label_main_announcements")
        self.announcements_textBrowser = QtWidgets.QTextBrowser(self.student_main)
        self.announcements_textBrowser.setGeometry(QtCore.QRect(10, 210, 811, 431))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.announcements_textBrowser.setFont(font)
        self.announcements_textBrowser.setStyleSheet("border-radius:10px;\n"
"border-color: rgb(197, 197, 226);\n"
"background-color: rgb(245, 245, 250);")
        self.announcements_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.announcements_textBrowser.setObjectName("announcements_textBrowser")
        self.tabWidget.addTab(self.student_main, "")
        self.student_profile = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(17)
        self.student_profile.setFont(font)
        self.student_profile.setObjectName("student_profile")
        self.label_profile_name = QtWidgets.QLabel(self.student_profile)
        self.label_profile_name.setGeometry(QtCore.QRect(181, 1, 250, 50))
        self.label_profile_name.setMinimumSize(QtCore.QSize(250, 50))
        self.label_profile_name.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_profile_name.setFont(font)
        self.label_profile_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_profile_name.setObjectName("label_profile_name")
        self.label_profile_surname = QtWidgets.QLabel(self.student_profile)
        self.label_profile_surname.setGeometry(QtCore.QRect(181, 115, 250, 50))
        self.label_profile_surname.setMinimumSize(QtCore.QSize(250, 50))
        self.label_profile_surname.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_profile_surname.setFont(font)
        self.label_profile_surname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_profile_surname.setObjectName("label_profile_surname")
        self.label_profile_birth = QtWidgets.QLabel(self.student_profile)
        self.label_profile_birth.setGeometry(QtCore.QRect(181, 229, 250, 50))
        self.label_profile_birth.setMinimumSize(QtCore.QSize(250, 50))
        self.label_profile_birth.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_profile_birth.setFont(font)
        self.label_profile_birth.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_profile_birth.setObjectName("label_profile_birth")
        self.label_profile_mail = QtWidgets.QLabel(self.student_profile)
        self.label_profile_mail.setGeometry(QtCore.QRect(181, 343, 250, 50))
        self.label_profile_mail.setMinimumSize(QtCore.QSize(250, 50))
        self.label_profile_mail.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_profile_mail.setFont(font)
        self.label_profile_mail.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_profile_mail.setObjectName("label_profile_mail")
        self.label_profile_city = QtWidgets.QLabel(self.student_profile)
        self.label_profile_city.setGeometry(QtCore.QRect(181, 457, 250, 50))
        self.label_profile_city.setMinimumSize(QtCore.QSize(250, 50))
        self.label_profile_city.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_profile_city.setFont(font)
        self.label_profile_city.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_profile_city.setObjectName("label_profile_city")
        self.label_profile_tel = QtWidgets.QLabel(self.student_profile)
        self.label_profile_tel.setGeometry(QtCore.QRect(181, 560, 250, 50))
        self.label_profile_tel.setMinimumSize(QtCore.QSize(250, 50))
        self.label_profile_tel.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_profile_tel.setFont(font)
        self.label_profile_tel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_profile_tel.setObjectName("label_profile_tel")
        self.student_profil_name_edit = QtWidgets.QTextEdit(self.student_profile)
        self.student_profil_name_edit.setGeometry(QtCore.QRect(181, 58, 450, 50))
        self.student_profil_name_edit.setMinimumSize(QtCore.QSize(450, 50))
        self.student_profil_name_edit.setMaximumSize(QtCore.QSize(450, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.student_profil_name_edit.setFont(font)
        self.student_profil_name_edit.setStyleSheet("background-color: rgb(245, 245, 250);\n"
"border-radius:10px;")
        self.student_profil_name_edit.setReadOnly(True)
        self.student_profil_name_edit.setOverwriteMode(False)
        self.student_profil_name_edit.setObjectName("student_profil_name_edit")
        self.student_profil_surname_edit = QtWidgets.QTextEdit(self.student_profile)
        self.student_profil_surname_edit.setGeometry(QtCore.QRect(181, 172, 450, 50))
        self.student_profil_surname_edit.setMinimumSize(QtCore.QSize(450, 50))
        self.student_profil_surname_edit.setMaximumSize(QtCore.QSize(450, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.student_profil_surname_edit.setFont(font)
        self.student_profil_surname_edit.setStyleSheet("background-color: rgb(245, 245, 250);\n"
"border-radius:10px;")
        self.student_profil_surname_edit.setReadOnly(True)
        self.student_profil_surname_edit.setOverwriteMode(False)
        self.student_profil_surname_edit.setObjectName("student_profil_surname_edit")
        self.student_profil_birth_edit = QtWidgets.QTextEdit(self.student_profile)
        self.student_profil_birth_edit.setGeometry(QtCore.QRect(181, 286, 450, 50))
        self.student_profil_birth_edit.setMinimumSize(QtCore.QSize(450, 50))
        self.student_profil_birth_edit.setMaximumSize(QtCore.QSize(450, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.student_profil_birth_edit.setFont(font)
        self.student_profil_birth_edit.setStyleSheet("background-color: rgb(245, 245, 250);\n"
"border-radius:10px;")
        self.student_profil_birth_edit.setReadOnly(True)
        self.student_profil_birth_edit.setOverwriteMode(False)
        self.student_profil_birth_edit.setObjectName("student_profil_birth_edit")
        self.student_profil_mail_edit = QtWidgets.QTextEdit(self.student_profile)
        self.student_profil_mail_edit.setGeometry(QtCore.QRect(181, 400, 450, 50))
        self.student_profil_mail_edit.setMinimumSize(QtCore.QSize(450, 50))
        self.student_profil_mail_edit.setMaximumSize(QtCore.QSize(450, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.student_profil_mail_edit.setFont(font)
        self.student_profil_mail_edit.setStyleSheet("background-color: rgb(245, 245, 250);\n"
"border-radius:10px;")
        self.student_profil_mail_edit.setReadOnly(True)
        self.student_profil_mail_edit.setOverwriteMode(False)
        self.student_profil_mail_edit.setObjectName("student_profil_mail_edit")
        self.student_profil_city_edit = QtWidgets.QTextEdit(self.student_profile)
        self.student_profil_city_edit.setGeometry(QtCore.QRect(181, 514, 450, 50))
        self.student_profil_city_edit.setMinimumSize(QtCore.QSize(450, 50))
        self.student_profil_city_edit.setMaximumSize(QtCore.QSize(450, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.student_profil_city_edit.setFont(font)
        self.student_profil_city_edit.setStyleSheet("background-color: rgb(245, 245, 250);\n"
"border-radius:10px;")
        self.student_profil_city_edit.setReadOnly(False)
        self.student_profil_city_edit.setOverwriteMode(False)
        self.student_profil_city_edit.setObjectName("student_profil_city_edit")
        self.student_profil_tel_edit = QtWidgets.QTextEdit(self.student_profile)
        self.student_profil_tel_edit.setGeometry(QtCore.QRect(181, 610, 450, 50))
        self.student_profil_tel_edit.setMinimumSize(QtCore.QSize(450, 50))
        self.student_profil_tel_edit.setMaximumSize(QtCore.QSize(450, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.student_profil_tel_edit.setFont(font)
        self.student_profil_tel_edit.setStyleSheet("background-color: rgb(245, 245, 250);\n"
"border-radius:10px;")
        self.student_profil_tel_edit.setReadOnly(False)
        self.student_profil_tel_edit.setOverwriteMode(False)
        self.student_profil_tel_edit.setObjectName("student_profil_tel_edit")
        self.update_information_Button = QtWidgets.QPushButton(self.student_profile)
        self.update_information_Button.setGeometry(QtCore.QRect(180, 670, 451, 50))
        self.update_information_Button.setMinimumSize(QtCore.QSize(270, 50))
        self.update_information_Button.setMaximumSize(QtCore.QSize(451, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.update_information_Button.setFont(font)
        self.update_information_Button.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(132, 132, 193);\n"
"color: rgb(255, 255, 255);")
        self.update_information_Button.setObjectName("update_information_Button")
        self.tabWidget.addTab(self.student_profile, "")
        self.student_plan = QtWidgets.QWidget()
        self.student_plan.setObjectName("student_plan")
        self.label_plan_lesson = QtWidgets.QLabel(self.student_plan)
        self.label_plan_lesson.setGeometry(QtCore.QRect(120, 30, 300, 50))
        self.label_plan_lesson.setMinimumSize(QtCore.QSize(300, 50))
        self.label_plan_lesson.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_plan_lesson.setFont(font)
        self.label_plan_lesson.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);")
        self.label_plan_lesson.setObjectName("label_plan_lesson")
        self.label_plan_mentor = QtWidgets.QLabel(self.student_plan)
        self.label_plan_mentor.setGeometry(QtCore.QRect(480, 30, 300, 50))
        self.label_plan_mentor.setMinimumSize(QtCore.QSize(300, 50))
        self.label_plan_mentor.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_plan_mentor.setFont(font)
        self.label_plan_mentor.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);")
        self.label_plan_mentor.setObjectName("label_plan_mentor")
        self.student_plan_lesson_list = QtWidgets.QTableWidget(self.student_plan)
        self.student_plan_lesson_list.setGeometry(QtCore.QRect(10, 90, 400, 500))
        self.student_plan_lesson_list.setMinimumSize(QtCore.QSize(0, 350))
        self.student_plan_lesson_list.setMaximumSize(QtCore.QSize(450, 500))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.student_plan_lesson_list.setFont(font)
        self.student_plan_lesson_list.setStyleSheet("background-color: rgb(245, 245, 250);\n"
"border-radius:10px;")
        self.student_plan_lesson_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.student_plan_lesson_list.setObjectName("student_plan_lesson_list")
        self.student_plan_lesson_list.setColumnCount(0)
        self.student_plan_lesson_list.setRowCount(0)
        self.student_plan_mentor_list = QtWidgets.QTableWidget(self.student_plan)
        self.student_plan_mentor_list.setGeometry(QtCore.QRect(440, 90, 400, 500))
        self.student_plan_mentor_list.setMinimumSize(QtCore.QSize(300, 350))
        self.student_plan_mentor_list.setMaximumSize(QtCore.QSize(450, 500))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.student_plan_mentor_list.setFont(font)
        self.student_plan_mentor_list.setStyleSheet("background-color: rgb(245, 245, 250);\n"
"border-radius:10px;")
        self.student_plan_mentor_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.student_plan_mentor_list.setObjectName("student_plan_mentor_list")
        self.student_plan_mentor_list.setColumnCount(0)
        self.student_plan_mentor_list.setRowCount(0)
        self.lesson_attendance = QtWidgets.QPushButton(self.student_plan)
        self.lesson_attendance.setGeometry(QtCore.QRect(80, 610, 270, 50))
        self.lesson_attendance.setMinimumSize(QtCore.QSize(270, 50))
        self.lesson_attendance.setMaximumSize(QtCore.QSize(270, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lesson_attendance.setFont(font)
        self.lesson_attendance.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(132, 132, 193);\n"
"color: rgb(255, 255, 255);")
        self.lesson_attendance.setObjectName("lesson_attendance")
        self.mentor_attendance = QtWidgets.QPushButton(self.student_plan)
        self.mentor_attendance.setGeometry(QtCore.QRect(500, 610, 270, 50))
        self.mentor_attendance.setMinimumSize(QtCore.QSize(270, 50))
        self.mentor_attendance.setMaximumSize(QtCore.QSize(270, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mentor_attendance.setFont(font)
        self.mentor_attendance.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(132, 132, 193);\n"
"color: rgb(255, 255, 255);")
        self.mentor_attendance.setObjectName("mentor_attendance")
        self.tabWidget.addTab(self.student_plan, "")
        self.student_to_do = QtWidgets.QWidget()
        self.student_to_do.setObjectName("student_to_do")
        self.update_status_button = QtWidgets.QPushButton(self.student_to_do)
        self.update_status_button.setGeometry(QtCore.QRect(300, 170, 113, 31))
        self.update_status_button.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(132, 132, 193);\n"
"color: rgb(255, 255, 255);")
        self.update_status_button.setObjectName("update_status_button")
        self.status_options = QtWidgets.QComboBox(self.student_to_do)
        self.status_options.setGeometry(QtCore.QRect(50, 170, 241, 26))
        self.status_options.setStyleSheet("border-radius:10px;\n"
"border-color: rgb(197, 197, 226);\n"
"background-color: rgb(245, 245, 250);")
        self.status_options.setObjectName("status_options")
        self.label = QtWidgets.QLabel(self.student_to_do)
        self.label.setGeometry(QtCore.QRect(260, 50, 391, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tasks_tableWidget = QtWidgets.QTableWidget(self.student_to_do)
        self.tasks_tableWidget.setGeometry(QtCore.QRect(50, 220, 761, 461))
        self.tasks_tableWidget.setStyleSheet("border-radius:10px;\n"
"border-color: rgb(197, 197, 226);\n"
"background-color: rgb(245, 245, 250);")
        self.tasks_tableWidget.setObjectName("tasks_tableWidget")
        self.tasks_tableWidget.setColumnCount(0)
        self.tasks_tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.student_to_do, "")
        self.student_attendance = QtWidgets.QWidget()
        self.student_attendance.setObjectName("student_attendance")
        self.label_lesson_status = QtWidgets.QLabel(self.student_attendance)
        self.label_lesson_status.setGeometry(QtCore.QRect(80, 30, 400, 50))
        self.label_lesson_status.setMinimumSize(QtCore.QSize(400, 50))
        self.label_lesson_status.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_lesson_status.setFont(font)
        self.label_lesson_status.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_lesson_status.setObjectName("label_lesson_status")
        self.student_attendance_lesson_list = QtWidgets.QTextEdit(self.student_attendance)
        self.student_attendance_lesson_list.setGeometry(QtCore.QRect(20, 90, 381, 500))
        self.student_attendance_lesson_list.setMinimumSize(QtCore.QSize(0, 0))
        self.student_attendance_lesson_list.setMaximumSize(QtCore.QSize(450, 500))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.student_attendance_lesson_list.setFont(font)
        self.student_attendance_lesson_list.setStyleSheet("background-color: rgb(245, 245, 250);\n"
"border-radius:10px;")
        self.student_attendance_lesson_list.setObjectName("student_attendance_lesson_list")
        self.label_mentor_status = QtWidgets.QLabel(self.student_attendance)
        self.label_mentor_status.setGeometry(QtCore.QRect(470, 30, 470, 50))
        self.label_mentor_status.setMinimumSize(QtCore.QSize(470, 50))
        self.label_mentor_status.setMaximumSize(QtCore.QSize(470, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_mentor_status.setFont(font)
        self.label_mentor_status.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_mentor_status.setObjectName("label_mentor_status")
        self.student_attendance_mentor_list = QtWidgets.QTextEdit(self.student_attendance)
        self.student_attendance_mentor_list.setGeometry(QtCore.QRect(450, 90, 381, 500))
        self.student_attendance_mentor_list.setMinimumSize(QtCore.QSize(0, 0))
        self.student_attendance_mentor_list.setMaximumSize(QtCore.QSize(450, 500))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.student_attendance_mentor_list.setFont(font)
        self.student_attendance_mentor_list.setStyleSheet("background-color: rgb(245, 245, 250);\n"
"border-radius:10px;")
        self.student_attendance_mentor_list.setObjectName("student_attendance_mentor_list")
        self.tabWidget.addTab(self.student_attendance, "")
        self.student_dance = QtWidgets.QWidget()
        self.student_dance.setObjectName("student_dance")
        self.chat_list = QtWidgets.QComboBox(self.student_dance)
        self.chat_list.setGeometry(QtCore.QRect(30, 30, 230, 50))
        self.chat_list.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.chat_list.setFont(font)
        self.chat_list.setStyleSheet("background-color: rgb(249, 186, 50);\n"
"color: rgb(0, 0, 0);")
        self.chat_list.setObjectName("chat_list")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.student_chat_message_panel = QtWidgets.QTextEdit(self.student_dance)
        self.student_chat_message_panel.setGeometry(QtCore.QRect(280, 30, 650, 400))
        self.student_chat_message_panel.setMinimumSize(QtCore.QSize(650, 400))
        self.student_chat_message_panel.setMaximumSize(QtCore.QSize(650, 400))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.student_chat_message_panel.setFont(font)
        self.student_chat_message_panel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.student_chat_message_panel.setObjectName("student_chat_message_panel")
        self.student_chat_message = QtWidgets.QTextEdit(self.student_dance)
        self.student_chat_message.setGeometry(QtCore.QRect(280, 470, 650, 100))
        self.student_chat_message.setMinimumSize(QtCore.QSize(650, 100))
        self.student_chat_message.setMaximumSize(QtCore.QSize(650, 100))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.student_chat_message.setFont(font)
        self.student_chat_message.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.student_chat_message.setObjectName("student_chat_message")
        self.student_chat_send_button = QtWidgets.QPushButton(self.student_dance)
        self.student_chat_send_button.setGeometry(QtCore.QRect(470, 590, 101, 50))
        self.student_chat_send_button.setMinimumSize(QtCore.QSize(50, 50))
        self.student_chat_send_button.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.student_chat_send_button.setFont(font)
        self.student_chat_send_button.setStyleSheet("background-color: rgb(249, 186, 50);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.student_chat_send_button.setObjectName("student_chat_send_button")
        self.tabWidget.addTab(self.student_dance, "")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 261, 811))
        self.label_8.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.935, y2:0.965909, stop:0 rgba(0, 0, 127, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 50, 201, 251))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.student_main_name = QtWidgets.QLabel(self.centralwidget)
        self.student_main_name.setGeometry(QtCore.QRect(30, 230, 201, 50))
        self.student_main_name.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.student_main_name.setFont(font)
        self.student_main_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(57, 57, 57);")
        self.student_main_name.setAlignment(QtCore.Qt.AlignCenter)
        self.student_main_name.setObjectName("student_main_name")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 157, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(57, 57, 57);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.user_avatar = QtWidgets.QLabel(self.centralwidget)
        self.user_avatar.setGeometry(QtCore.QRect(80, 80, 101, 50))
        self.user_avatar.setStyleSheet("color: rgb(57, 57, 57);")
        self.user_avatar.setObjectName("user_avatar")
        self.chat_student_button = QtWidgets.QPushButton(self.centralwidget)
        self.chat_student_button.setGeometry(QtCore.QRect(60, 510, 150, 100))
        self.chat_student_button.setMinimumSize(QtCore.QSize(150, 100))
        self.chat_student_button.setMaximumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.chat_student_button.setFont(font)
        self.chat_student_button.setStyleSheet("background-color: transparent")
        self.chat_student_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./sign/assets/comments.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chat_student_button.setIcon(icon)
        self.chat_student_button.setIconSize(QtCore.QSize(100, 100))
        self.chat_student_button.setObjectName("chat_student_button")
        self.signout_button = QtWidgets.QPushButton(self.centralwidget)
        self.signout_button.setGeometry(QtCore.QRect(90, 670, 83, 79))
        self.signout_button.setStyleSheet("background-color:transparent;")
        self.signout_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./sign/assets/signout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signout_button.setIcon(icon1)
        self.signout_button.setIconSize(QtCore.QSize(70, 70))
        self.signout_button.setObjectName("signout_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.student_main_date.setText(_translate("MainWindow", "26/12/2023"))
        self.label_main_announcements.setText(_translate("MainWindow", "Announcements"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_main), _translate("MainWindow", "Main"))
        self.label_profile_name.setText(_translate("MainWindow", "Name :"))
        self.label_profile_surname.setText(_translate("MainWindow", "Surname :"))
        self.label_profile_birth.setText(_translate("MainWindow", "Date of Birth :"))
        self.label_profile_mail.setText(_translate("MainWindow", "E-Mail :"))
        self.label_profile_city.setText(_translate("MainWindow", "City :"))
        self.label_profile_tel.setText(_translate("MainWindow", "Tel :"))
        self.update_information_Button.setText(_translate("MainWindow", "Update Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_profile), _translate("MainWindow", "Profile"))
        self.label_plan_lesson.setText(_translate("MainWindow", "Lesson Plan"))
        self.label_plan_mentor.setText(_translate("MainWindow", "Mentor Meeting Plan"))
        self.lesson_attendance.setText(_translate("MainWindow", "Lesson Attendance"))
        self.mentor_attendance.setText(_translate("MainWindow", "Mentor Attendance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_plan), _translate("MainWindow", "Lesson / Mentor Plan"))
        self.update_status_button.setText(_translate("MainWindow", "Update Status"))
        self.label.setText(_translate("MainWindow", "Student to do List"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_to_do), _translate("MainWindow", "To do List"))
        self.label_lesson_status.setText(_translate("MainWindow", "Lesson Attendance Status"))
        self.label_mentor_status.setText(_translate("MainWindow", "Mentor Meeting Attendance Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_attendance), _translate("MainWindow", "Attendance Status"))
        self.chat_list.setItemText(0, _translate("MainWindow", "Please Select Person:"))
        self.chat_list.setItemText(1, _translate("MainWindow", "None"))
        self.chat_list.setItemText(2, _translate("MainWindow", "None"))
        self.chat_list.setItemText(3, _translate("MainWindow", "None"))
        self.chat_list.setItemText(4, _translate("MainWindow", "None"))
        self.chat_list.setItemText(5, _translate("MainWindow", "None"))
        self.chat_list.setItemText(6, _translate("MainWindow", "None"))
        self.chat_list.setItemText(7, _translate("MainWindow", "None"))
        self.chat_list.setItemText(8, _translate("MainWindow", "None"))
        self.chat_list.setItemText(9, _translate("MainWindow", "None"))
        self.chat_list.setItemText(10, _translate("MainWindow", "None"))
        self.student_chat_send_button.setText(_translate("MainWindow", "SEND"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_dance), _translate("MainWindow", "Chat"))
        self.student_main_name.setText(_translate("MainWindow", " AHMET"))
        self.label_6.setText(_translate("MainWindow", "WELCOME"))
        self.user_avatar.setText(_translate("MainWindow", "avatar"))
