from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_form_update_balance_user import * 
from collab_with_base import *

class DialogUpdateBalanceUser(QDialog, DataBase):
    def __init__(self, parent=None):
        super(DialogUpdateBalanceUser, self).__init__(parent)
        self.ui = Ui_Dialog_updateBalance_master()
        self.setWindowTitle('Обновление баланса')
        self.ui.setupUi(self)
        self.set_connect()
        self.ui.btn_update_balance.clicked.connect(self.update_balance)
        self.ui.le_user_balance.setValidator(QDoubleValidator())
    
    def update_balance(self): 
        '''
        Реализует логику обновления баланса с помощью абстракции set_data_user_balance_update
        '''
        
        try: 
            user_login = self.ui.le_target_user.text()
            user_balance = self.ui.le_user_balance.text()
            if user_login != '' and user_balance != '': 
                data = self.set_data_user_balance_update(user_balance, user_login)
                if data == 1: 
                    QMessageBox.information(QMessageBox(), 'Обновление', 'Обновление прошло успешно')
                else:
                    raise
            else:
                QMessageBox.information(QMessageBox(), 'Обновление', 'Одно из полей не заполненно')
        except Exception: 
            QMessageBox.warning(QMessageBox(), 'Обновление', 'Непредвиденная ошибка\nТакого пользователя не существует')
            