# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_shopKFEBjC.ui'
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 120, 401))
        self.frame.setStyleSheet(u"background-color: rgb(55, 55, 55);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_goto_shop = QPushButton(self.frame)
        self.btn_goto_shop.setObjectName(u"btn_goto_shop")
        self.btn_goto_shop.setGeometry(QRect(0, 55, 121, 51))
        self.btn_goto_shop.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgb(55,55,55);\n"
"border: 0px, solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: gray;\n"
"}")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 10, 111, 41))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_got_account = QPushButton(self.frame)
        self.btn_got_account.setObjectName(u"btn_got_account")
        self.btn_got_account.setGeometry(QRect(0, 110, 121, 51))
        self.btn_got_account.setStyleSheet(u"QPushButton {\n"
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
        self.page_shop = QWidget()
        self.page_shop.setObjectName(u"page_shop")
        self.label_2 = QLabel(self.page_shop)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, -10, 91, 31))
        font = QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.tableWidget_view_shop = QTableWidget(self.page_shop)
        self.tableWidget_view_shop.setObjectName(u"tableWidget_view_shop")
        self.tableWidget_view_shop.setGeometry(QRect(5, 71, 651, 251))
        self.tableWidget_view_shop.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.btn_buy_product = QPushButton(self.page_shop)
        self.btn_buy_product.setObjectName(u"btn_buy_product")
        self.btn_buy_product.setGeometry(QRect(4, 22, 121, 41))
        self.btn_buy_product.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgb(55,55,55);\n"
"border: 0px, solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: gray;\n"
"}")
        self.label_view_balance = QLabel(self.page_shop)
        self.label_view_balance.setObjectName(u"label_view_balance")
        self.label_view_balance.setGeometry(QRect(386, 22, 261, 31))
        self.label_view_balance.setFont(font)
        self.stackedWidget.addWidget(self.page_shop)
        self.page_account = QWidget()
        self.page_account.setObjectName(u"page_account")
        self.label_hello_customer = QLabel(self.page_account)
        self.label_hello_customer.setObjectName(u"label_hello_customer")
        self.label_hello_customer.setGeometry(QRect(4, 32, 471, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_hello_customer.setFont(font1)
        self.label_4 = QLabel(self.page_account)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 0, 151, 31))
        self.label_4.setFont(font)
        self.tableWidget_view_deals = QTableWidget(self.page_account)
        self.tableWidget_view_deals.setObjectName(u"tableWidget_view_deals")
        self.tableWidget_view_deals.setGeometry(QRect(5, 71, 651, 251))
        self.stackedWidget.addWidget(self.page_account)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_goto_shop.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0433\u0430\u0437\u0438\u043d", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">\u041f\u0430\u043d\u0435\u043b\u044c</span></p><p align=\"center\"><span style=\" font-size:10pt;\">\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f</span></p></body></html>", None))
        self.btn_got_account.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041c\u0430\u0433\u0430\u0437\u0438\u043d</p></body></html>", None))
        self.btn_buy_product.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u043f\u0438\u0442\u044c", None))
        self.label_view_balance.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_hello_customer.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0417\u0434\u0440\u0430\u0432\u0441\u0442\u0432\u0443\u0439\u0442\u0435, </p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442</p></body></html>", None))
    # retranslateUi

