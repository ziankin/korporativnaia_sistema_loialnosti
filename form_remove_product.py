from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_form_remove_product import * 
from collab_with_base import *


class DialogRemoveProduct(QDialog, DataBase):
    def __init__(self, parent=None):
        super(DialogRemoveProduct, self).__init__(parent)
        self.ui = Ui_Dialog_removeProduct_master()
        self.ui.setupUi(self)
        self.setWindowTitle('Удание товара')
        self.set_connect()
        self.ui.btn_remove_product.clicked.connect(self.remove_product)
        self.ui.le_product_id_for_delete.setValidator(QDoubleValidator())
         
    def remove_product(self): 
        '''
        Метод удаления товара. Ссылается на метод remove_data_product.
        '''  
         
        try: 
            product_id = self.ui.le_product_id_for_delete.text()
            product_name = self.ui.le_product_name_for_delete.text()
            data = self.remove_data_product(product_id, product_name)
            if data == 1:  
                QMessageBox.information(QMessageBox(), 'Удаление', 'Удаление прошло успешно')
            else:
                raise
        except Exception: 
            QMessageBox.warning(QMessageBox(), 'Удаление', 'Непредвиденная ошибка\nОшибка возникает: \nСсылка на товар который находится в транзакции\nНе вверный ввод\nНе все поля заполненны')