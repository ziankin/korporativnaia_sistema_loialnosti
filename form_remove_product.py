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
        validator_id = QDoubleValidator
        self.ui.le_product_id_for_delete.setValidator(validator_id)
         
    def remove_product(self): 
        try: 
            product_id = self.ui.le_product_id_for_delete.text()
            product_name = self.ui.le_product_name_for_delete.text()
            self.remove_data_product(product_id, product_name)
            QMessageBox.information(QMessageBox(), 'Удаление', 'Удаление прошло успешно')
        except Exception: 
            QMessageBox.warning(QMessageBox(), 'Удаление', 'Непредвиденная ошибка')