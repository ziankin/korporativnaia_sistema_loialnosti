import sys 
from PySide2.QtCore import *
from PySide2.QtCore import QTimer
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit
from ui_form_admin import * 
from collab_with_base import *
from form_insert_product import *
from form_remove_product import * 
from form_update_balance_user import * 


class MainWindow_admin(QMainWindow, DataBase):
    def __init__(self, parent=None):
        super(MainWindow_admin, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.windowTitle('Панель администратора')
        self.set_connect()
        self.filling_table_product_admin()
        self.filling_table_users_admin()
        self.ui.btn_shop_manage.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_shop_admin) )
        self.ui.btn_user_manage.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_user_manage))
        self.ui.btn_insert_record.clicked.connect(self.calling_master_add)
        self.ui.btn_remove_record.clicked.connect(self.calling_remove_master)
        self.ui.btn_update_balance.clicked.connect(self.calling_update_balance_master)
        self.ui.tablewidget_shop_admin.setHorizontalHeaderLabels(['id продукта', 'Название', 'Цена'])
        self.ui.tablewidget_manage_users.setHorizontalHeaderLabels(['id пользователя', 'Логин', 'Пароль','Администратор','Баланс'])
      
    def filling_table_product_admin(self): 
        products = self.get_data_product()
        products_rows = len(products)
        products_columns = len(products[0])
        self.ui.tablewidget_shop_admin.setRowCount(products_rows)
        self.ui.tablewidget_shop_admin.setColumnCount(products_columns)
        for i in range(products_rows): 
            for j in range(products_columns): 
                item = QTableWidgetItem(f"{products[i][j]}")
                self.ui.tablewidget_shop_admin.setItem(i, j, item) 
        
        QTimer.singleShot(10000, self.filling_table_product_admin)
    
    def filling_table_users_admin(self): 
        users = self.get_data_users()
        users_rows = len(users)
        users_columns = len(users[0])
        self.ui.tablewidget_manage_users.setRowCount(users_rows)
        self.ui.tablewidget_manage_users.setColumnCount(users_columns)
        for i in range(users_rows): 
            for j in range(users_columns): 
                item = QTableWidgetItem(f"{users[i][j]}")
                self.ui.tablewidget_manage_users.setItem(i, j, item) 
        
        QTimer.singleShot(10000, self.filling_table_users_admin)

    def calling_master_add(self): 
        dialog_insert_product = DialogInsertProduct()
        dialog_insert_product.show()
        dialog_insert_product.exec_()
        self.filling_table_product_admin()
        
    def calling_remove_master(self): 
        dialog_remove_product = DialogRemoveProduct()
        dialog_remove_product.show()
        dialog_remove_product.exec_()
        self.filling_table_product_admin()
    
    def calling_update_balance_master(self): 
        dialog_update_balance = DialogUpdateBalanceUser()
        dialog_update_balance.show()
        dialog_update_balance.exec_()
        self.filling_table_users_admin()
        
        
