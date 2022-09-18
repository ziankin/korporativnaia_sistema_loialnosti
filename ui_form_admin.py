# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_adminvTjWkV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setMinimumSize(QSize(800, 400))
        MainWindow.setMaximumSize(QSize(800, 400))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 120, 401))
        self.frame.setStyleSheet(u"background-color: rgb(55, 55, 55);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_shop_manage = QPushButton(self.frame)
        self.btn_shop_manage.setObjectName(u"btn_shop_manage")
        self.btn_shop_manage.setGeometry(QRect(0, 55, 121, 51))
        self.btn_shop_manage.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgb(55,55,55);\n"
"border: 0px, solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: gray;\n"
"}")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(5, 0, 111, 51))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_user_manage = QPushButton(self.frame)
        self.btn_user_manage.setObjectName(u"btn_user_manage")
        self.btn_user_manage.setGeometry(QRect(0, 110, 121, 51))
        self.btn_user_manage.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgb(55,55,55);\n"
"border: 0px, solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: gray;\n"
"}")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(120, 0, 681, 51))
        self.frame_2.setStyleSheet(u"background-color: rgb(55, 55, 55);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(129, 59, 661, 331))
        self.page_shop_admin = QWidget()
        self.page_shop_admin.setObjectName(u"page_shop_admin")
        self.btn_insert_record = QPushButton(self.page_shop_admin)
        self.btn_insert_record.setObjectName(u"btn_insert_record")
        self.btn_insert_record.setGeometry(QRect(0, 60, 121, 41))
        self.btn_insert_record.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgb(55,55,55);\n"
"border: 0px, solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: gray;\n"
"}")
        self.btn_remove_record = QPushButton(self.page_shop_admin)
        self.btn_remove_record.setObjectName(u"btn_remove_record")
        self.btn_remove_record.setGeometry(QRect(0, 110, 121, 41))
        self.btn_remove_record.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgb(55,55,55);\n"
"border: 0px, solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: gray;\n"
"}")
        self.label_3 = QLabel(self.page_shop_admin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 121, 41))
        font = QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.tablewidget_shop_admin = QTableWidget(self.page_shop_admin)
        self.tablewidget_shop_admin.setObjectName(u"tablewidget_shop_admin")
        self.tablewidget_shop_admin.setGeometry(QRect(125, 11, 531, 311))
        self.stackedWidget.addWidget(self.page_shop_admin)
        self.page_user_manage = QWidget()
        self.page_user_manage.setObjectName(u"page_user_manage")
        self.label_4 = QLabel(self.page_user_manage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 10, 151, 71))
        self.label_4.setFont(font)
        self.btn_update_balance = QPushButton(self.page_user_manage)
        self.btn_update_balance.setObjectName(u"btn_update_balance")
        self.btn_update_balance.setGeometry(QRect(0, 85, 141, 41))
        self.btn_update_balance.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgb(55,55,55);\n"
"border: 0px, solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: gray;\n"
"}")
        self.tablewidget_manage_users = QTableWidget(self.page_user_manage)
        self.tablewidget_manage_users.setObjectName(u"tablewidget_manage_users")
        self.tablewidget_manage_users.setGeometry(QRect(155, 11, 501, 311))
        self.stackedWidget.addWidget(self.page_user_manage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_shop_manage.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435\n"
"\u043c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u043c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">\u041f\u0430\u043d\u0435\u043b\u044c</span></p><p align=\"center\"><span style=\" font-size:10pt;\">\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430</span></p></body></html>", None))
        self.btn_user_manage.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435\n"
"\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.btn_insert_record.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0441\u044c", None))
        self.btn_remove_record.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041c\u0430\u0433\u0430\u0437\u0438\u043d</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 </p><p>\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c\u0438</p></body></html>", None))
        self.btn_update_balance.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0431\u0430\u043b\u0430\u043d\u0441", None))
    # retranslateUi

