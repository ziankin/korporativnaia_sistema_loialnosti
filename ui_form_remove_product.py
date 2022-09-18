# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_remove_productxdftYX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_removeProduct_master(object):
    def setupUi(self, Dialog_removeProduct_master):
        if not Dialog_removeProduct_master.objectName():
            Dialog_removeProduct_master.setObjectName(u"Dialog_removeProduct_master")
        Dialog_removeProduct_master.resize(378, 211)
        Dialog_removeProduct_master.setMinimumSize(QSize(378, 211))
        Dialog_removeProduct_master.setMaximumSize(QSize(378, 211))
        self.btn_remove_product = QPushButton(Dialog_removeProduct_master)
        self.btn_remove_product.setObjectName(u"btn_remove_product")
        self.btn_remove_product.setGeometry(QRect(140, 160, 101, 41))
        self.le_product_id_for_delete = QLineEdit(Dialog_removeProduct_master)
        self.le_product_id_for_delete.setObjectName(u"le_product_id_for_delete")
        self.le_product_id_for_delete.setGeometry(QRect(52, 80, 271, 31))
        self.le_product_name_for_delete = QLineEdit(Dialog_removeProduct_master)
        self.le_product_name_for_delete.setObjectName(u"le_product_name_for_delete")
        self.le_product_name_for_delete.setGeometry(QRect(52, 119, 271, 31))
        self.label = QLabel(Dialog_removeProduct_master)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 271, 61))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.retranslateUi(Dialog_removeProduct_master)

        QMetaObject.connectSlotsByName(Dialog_removeProduct_master)
    # setupUi

    def retranslateUi(self, Dialog_removeProduct_master):
        Dialog_removeProduct_master.setWindowTitle(QCoreApplication.translate("Dialog_removeProduct_master", u"Dialog", None))
        self.btn_remove_product.setText(QCoreApplication.translate("Dialog_removeProduct_master", u"\u041e\u043a", None))
        self.le_product_id_for_delete.setPlaceholderText(QCoreApplication.translate("Dialog_removeProduct_master", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.le_product_name_for_delete.setPlaceholderText(QCoreApplication.translate("Dialog_removeProduct_master", u"\u0422\u043e\u0432\u0430\u0440", None))
        self.label.setText(QCoreApplication.translate("Dialog_removeProduct_master", u"<html><head/><body><p align=\"center\">\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430</p></body></html>", None))
    # retranslateUi

