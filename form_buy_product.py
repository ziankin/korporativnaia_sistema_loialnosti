from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_form_buy_product import * 
from collab_with_base import *


class BuyProduct(QDialog, DataBase):
    def __init__(self, login_user ,parent=None):
        super(BuyProduct, self).__init__(parent)
        self.ui = Ui_Form_shopping_master()
        self.setWindowTitle('Покупка')
        self.user_log = login_user
        self.ui.setupUi(self)
        self.set_connect()
        self.ui.btn_buyproduct.clicked.connect(self.buy_product)


    def buy_product(self): 
        try: 
            product = self.ui.lineEdit_name_product.text()
            if (len(product) != 0): 
                if self.set_data_deal(self.user_log, product) == 1: 
                    self.set_calculate_user_balance(self.user_log)
                    QMessageBox.information(QMessageBox(), 'Покупка', 'Покупка прошла успешно')
                else: 
                    raise TypeError
            else:
                raise TypeError
            
        except TypeError: 
            QMessageBox.warning(QMessageBox(), 'Покупка', 'Непредвиденная ошибка')