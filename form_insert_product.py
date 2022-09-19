from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_form_insert_product import * 
from collab_with_base import *


class DialogInsertProduct(QDialog, DataBase):
    def __init__(self, parent=None):
        super(DialogInsertProduct, self).__init__(parent)
        self.ui = Ui_Dialog_addProduct_master()
        self.setWindowTitle('Добавление товара')
        self.ui.setupUi(self)
        self.set_connect()
        self.ui.btn_add_product.clicked.connect(self.insert_product)
        validator_cost = QDoubleValidator
        self.ui.le_product_cost.setValidator(validator_cost)
    
    def insert_product(self): 
        try: 
            product_name = self.ui.le_product_name.text()
            product_cost = self.ui.le_product_cost.text()
            if product_name != '' and product_cost != '': 
                self.set_new_data_product(product_name, product_cost)
                QMessageBox.information(QMessageBox(), 'Добавление', 'Добавление прошло успешно')
            else: 
                QMessageBox.information(QMessageBox(), 'Добавление', 'Одно из полей не заполненно')
        except Exception:
             QMessageBox.warning(QMessageBox(), 'Добавление', 'Непредвиденная ошибка')
        