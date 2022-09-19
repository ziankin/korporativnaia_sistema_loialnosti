from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit
from ui_form_shop import *
from collab_with_base import *
from form_authorisation import Dialog
from form_buy_product import * 


class MainWindow_shop(QMainWindow, DataBase):
    def __init__(self, login, parent=None):
        super(MainWindow_shop, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Магазин')
        self.usr_log = login 
        self.set_connect() 
        self.filling_table_product()
        self.filling_table_order()
        self.view_current_balance()
        self.ui.tableWidget_view_shop.setHorizontalHeaderLabels(['id товара', 'Название', 'Цена'])
        self.ui.tableWidget_view_deals.setHorizontalHeaderLabels(['Пользователь', 'Название товара', 'Цена', 'Время покупки'])
        self.ui.btn_goto_shop.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_shop))
        self.ui.btn_got_account.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_account))
        self.ui.btn_buy_product.clicked.connect(self.buy_product)

    def filling_table_product(self):
        products = self.get_data_product()
        products_rows = len(products)
        products_columns = len(products[0])
        self.ui.tableWidget_view_shop.setRowCount(products_rows)
        self.ui.tableWidget_view_shop.setColumnCount(products_columns)
        for i in range(products_rows): 
            for j in range(products_columns): 
                item = QTableWidgetItem(f"{products[i][j]}")
                self.ui.tableWidget_view_shop.setItem(i, j, item) 
        
        QTimer.singleShot(10000, self.filling_table_product)
    
    def filling_table_order(self): 
        deals = self.get_data_deal(self.usr_log)
        if len(deals) != 0: 
            deals_rows = len(deals)
            deals_columns = len(deals[0])
            self.ui.tableWidget_view_deals.setRowCount(deals_rows)
            self.ui.tableWidget_view_deals.setColumnCount(deals_columns)
            for i in range(deals_rows): 
                for j in range(deals_columns): 
                    item = QTableWidgetItem(f"{deals[i][j]}")
                    self.ui.tableWidget_view_deals.setItem(i, j, item) 
            self.ui.label_hello_customer.setText(f"Здравствуйте, {self.usr_log} ваши покупки: ")
            QTimer.singleShot(10000, self.filling_table_order)
        else: 
            self.ui.label_hello_customer.setText(f"Здравствуйте, {self.usr_log} вы, еще не совершали покупок")
    
    def view_current_balance(self):
        balance = self.set_calculate_user_balance(self.usr_log)
        self.ui.label_view_balance.setText(f"Текущий баланс {balance}")
     
    def buy_product(self): 
        dialog_insert_product = BuyProduct(self.usr_log)
        dialog_insert_product.show()
        dialog_insert_product.exec_()
        self.filling_table_order()
        self.view_current_balance()
        

