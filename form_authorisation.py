import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_form_auth import *
from form_admin import *
from form_shop import *
from collab_with_base import *


class Dialog(QDialog, DataBase):
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Окно авторизации')
        self.set_connect() 
        self.ui.button_reqest_auth.clicked.connect(self.get_authorisation)
        self.ui.button_reqest_registration.clicked.connect(self.get_registration)

    def clear(self):
        self.ui.lined_login_form.clear()
        self.ui.lined_password_form.clear()

    def set_moving_shop(self):
        window = MainWindow_shop(self.ui.lined_login_form.text())
        window.show()
        
    def set_moving_admin(self):
        admin_panel = MainWindow_admin()
        admin_panel.show()

    def get_move(self, flag: int):
        self.ui.label_connection_infromation.setText('Авторизация успешна') 
        self.accept()
        self.set_moving_admin() if (flag == 1) else self.set_moving_shop()

    def set_login_details(self): 
        user_login = self.ui.lined_login_form.text()
        user_password = self.ui.lined_password_form.text()
        return user_login, user_password

    def get_authorisation(self):
        try:
            user_login, user_password = self.set_login_details()
            data = self.set_authorisation(user_login, user_password)

            if (len(user_login) != 0) and (len(user_password) != 0):
                if (data[0] == user_login) and (data[1] == user_password) and (data[2] == False):
                    self.get_move(0)

                elif (data[0] == user_login) and (data[1] == user_password) and (data[2] == True):
                    self.get_move(1)
                else:
                    raise TypeError
                
        except TypeError:
            QMessageBox.warning(QMessageBox(), 'Ошибка','Такого пользователя не существует')

    def get_registration(self):
        try:
            user_login, user_password = self.set_login_details()

            if (len(user_login) != 0) and (len(user_password) != 0):
                self.set_registration(user_login, user_password)
                self.get_move(0)
            else:
                raise
        except:
            QMessageBox.warning(QMessageBox(), 'Ошибка','Непредвиденная ошибка')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dialog()
    
    window.show()
    sys.exit(app.exec_())
