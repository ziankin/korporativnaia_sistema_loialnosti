# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_update_balance_usercaPmon.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_updateBalance_master(object):
    def setupUi(self, Dialog_updateBalance_master):
        if not Dialog_updateBalance_master.objectName():
            Dialog_updateBalance_master.setObjectName(u"Dialog_updateBalance_master")
        Dialog_updateBalance_master.resize(379, 211)
        Dialog_updateBalance_master.setMinimumSize(QSize(379, 211))
        Dialog_updateBalance_master.setMaximumSize(QSize(379, 211))
        self.le_target_user = QLineEdit(Dialog_updateBalance_master)
        self.le_target_user.setObjectName(u"le_target_user")
        self.le_target_user.setGeometry(QRect(50, 70, 271, 31))
        self.label_2 = QLabel(Dialog_updateBalance_master)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(38, 10, 271, 61))
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.le_user_balance = QLineEdit(Dialog_updateBalance_master)
        self.le_user_balance.setObjectName(u"le_user_balance")
        self.le_user_balance.setGeometry(QRect(50, 109, 271, 31))
        self.btn_update_balance = QPushButton(Dialog_updateBalance_master)
        self.btn_update_balance.setObjectName(u"btn_update_balance")
        self.btn_update_balance.setGeometry(QRect(138, 150, 101, 41))

        self.retranslateUi(Dialog_updateBalance_master)

        QMetaObject.connectSlotsByName(Dialog_updateBalance_master)
    # setupUi

    def retranslateUi(self, Dialog_updateBalance_master):
        Dialog_updateBalance_master.setWindowTitle(QCoreApplication.translate("Dialog_updateBalance_master", u"Dialog", None))
        self.le_target_user.setPlaceholderText(QCoreApplication.translate("Dialog_updateBalance_master", u"\u041b\u043e\u0433\u0438\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_updateBalance_master", u"<html><head/><body><p align=\"center\">\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0431\u0430\u043b\u0430\u043d\u0441\u0430</p></body></html>", None))
        self.le_user_balance.setPlaceholderText(QCoreApplication.translate("Dialog_updateBalance_master", u"\u0411\u0430\u043b\u0430\u043d\u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.btn_update_balance.setText(QCoreApplication.translate("Dialog_updateBalance_master", u"\u041e\u043a", None))
    # retranslateUi

