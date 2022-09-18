# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_buy_productLSFtCv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_shopping_master(object):
    def setupUi(self, Form_shopping_master):
        if not Form_shopping_master.objectName():
            Form_shopping_master.setObjectName(u"Form_shopping_master")
        Form_shopping_master.resize(251, 115)
        Form_shopping_master.setMinimumSize(QSize(251, 115))
        Form_shopping_master.setMaximumSize(QSize(251, 115))
        self.btn_buyproduct = QPushButton(Form_shopping_master)
        self.btn_buyproduct.setObjectName(u"btn_buyproduct")
        self.btn_buyproduct.setGeometry(QRect(80, 60, 91, 41))
        self.lineEdit_name_product = QLineEdit(Form_shopping_master)
        self.lineEdit_name_product.setObjectName(u"lineEdit_name_product")
        self.lineEdit_name_product.setGeometry(QRect(20, 20, 211, 31))

        self.retranslateUi(Form_shopping_master)

        QMetaObject.connectSlotsByName(Form_shopping_master)
    # setupUi

    def retranslateUi(self, Form_shopping_master):
        Form_shopping_master.setWindowTitle(QCoreApplication.translate("Form_shopping_master", u"Dialog", None))
        self.btn_buyproduct.setText(QCoreApplication.translate("Form_shopping_master", u"\u041e\u041a", None))
        self.lineEdit_name_product.setPlaceholderText(QCoreApplication.translate("Form_shopping_master", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
    # retranslateUi

