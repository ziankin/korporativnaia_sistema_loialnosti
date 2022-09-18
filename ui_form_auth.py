# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_authuyHzdt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(378, 290)
        Dialog.setMinimumSize(QSize(378, 290))
        Dialog.setMaximumSize(QSize(378, 290))
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.button_reqest_auth = QPushButton(Dialog)
        self.button_reqest_auth.setObjectName(u"button_reqest_auth")
        self.button_reqest_auth.setGeometry(QRect(30, 190, 101, 41))
        font = QFont()
        font.setPointSize(12)
        self.button_reqest_auth.setFont(font)
        self.button_reqest_auth.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: white;\n"
"border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: gray;\n"
"}")
        self.label_for_auth = QLabel(Dialog)
        self.label_for_auth.setObjectName(u"label_for_auth")
        self.label_for_auth.setGeometry(QRect(70, 30, 241, 41))
        self.lined_login_form = QLineEdit(Dialog)
        self.lined_login_form.setObjectName(u"lined_login_form")
        self.lined_login_form.setGeometry(QRect(30, 100, 321, 31))
        self.lined_login_form.setFont(font)
        self.lined_login_form.setStyleSheet(u"border: 1px solid;")
        self.lined_password_form = QLineEdit(Dialog)
        self.lined_password_form.setObjectName(u"lined_password_form")
        self.lined_password_form.setGeometry(QRect(30, 145, 321, 31))
        self.lined_password_form.setFont(font)
        self.lined_password_form.setStyleSheet(u"border: 1px solid;")
        self.button_reqest_registration = QPushButton(Dialog)
        self.button_reqest_registration.setObjectName(u"button_reqest_registration")
        self.button_reqest_registration.setGeometry(QRect(250, 190, 101, 41))
        self.button_reqest_registration.setFont(font)
        self.button_reqest_registration.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: white;\n"
"border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: gray;\n"
"}")
        self.label_connection_infromation = QLabel(Dialog)
        self.label_connection_infromation.setObjectName(u"label_connection_infromation")
        self.label_connection_infromation.setGeometry(QRect(30, 240, 321, 31))
        self.label_connection_infromation.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.button_reqest_auth.setText(QCoreApplication.translate("Dialog", u"\u0412\u0445\u043e\u0434", None))
        self.label_for_auth.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:26pt;\">\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443</span></p></body></html>", None))
        self.lined_login_form.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lined_password_form.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.button_reqest_registration.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_connection_infromation.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

