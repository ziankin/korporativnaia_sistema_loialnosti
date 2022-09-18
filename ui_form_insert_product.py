# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_insert_productcwPGIb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_addProduct_master(object):
    def setupUi(self, Dialog_addProduct_master):
        if not Dialog_addProduct_master.objectName():
            Dialog_addProduct_master.setObjectName(u"Dialog_addProduct_master")
        Dialog_addProduct_master.resize(379, 219)
        Dialog_addProduct_master.setMinimumSize(QSize(379, 219))
        Dialog_addProduct_master.setMaximumSize(QSize(379, 219))
        self.btn_add_product = QPushButton(Dialog_addProduct_master)
        self.btn_add_product.setObjectName(u"btn_add_product")
        self.btn_add_product.setGeometry(QRect(140, 150, 101, 41))
        self.le_product_name = QLineEdit(Dialog_addProduct_master)
        self.le_product_name.setObjectName(u"le_product_name")
        self.le_product_name.setGeometry(QRect(52, 70, 271, 31))
        self.le_product_cost = QLineEdit(Dialog_addProduct_master)
        self.le_product_cost.setObjectName(u"le_product_cost")
        self.le_product_cost.setGeometry(QRect(52, 109, 271, 31))
        self.label = QLabel(Dialog_addProduct_master)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 271, 61))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.retranslateUi(Dialog_addProduct_master)

        QMetaObject.connectSlotsByName(Dialog_addProduct_master)
    # setupUi

    def retranslateUi(self, Dialog_addProduct_master):
        Dialog_addProduct_master.setWindowTitle(QCoreApplication.translate("Dialog_addProduct_master", u"Dialog", None))
        self.btn_add_product.setText(QCoreApplication.translate("Dialog_addProduct_master", u"\u041e\u043a", None))
        self.le_product_name.setPlaceholderText(QCoreApplication.translate("Dialog_addProduct_master", u"\u0422\u043e\u0432\u0430\u0440", None))
        self.le_product_cost.setPlaceholderText(QCoreApplication.translate("Dialog_addProduct_master", u"\u0426\u0435\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog_addProduct_master", u"<html><head/><body><p align=\"center\">\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430</p></body></html>", None))
    # retranslateUi

