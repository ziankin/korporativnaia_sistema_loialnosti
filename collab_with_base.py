import configparser
import psycopg2

config = configparser.ConfigParser()
config.read('config.ini')


class DataBase():
    
    def set_connect(self): 
        self.conn = psycopg2.connect(
            database=config['database']['dbname'],
            user=config['database']['user'],
            password=config['database']['password'],
            host=config['database']['host'],
            port=config['database']['port']
        )

        self.cur = self.conn.cursor()
        
    def set_authorisation(self, user_login: str, user_password: str):
        '''
        Служит для авторизации пользователя. Выполняет SQL запрос на выборку.
        
        param: 
            - user_login : str
            - user_password : str
        
        return: 
            tuple
        
        '''
        data = self.cur.execute(f"""SELECT user_login, user_password, user_role_admin FROM users" 
                                "WHERE user_login='{user_login}' and user_password='{user_password}'""") 

        data = self.cur.fetchone()
        return data
    
    def set_registration(self, user_login: str, user_password: str):
        '''
        Служит для регистрации пользователя. Выполняет SQL запрос на выборку.
        Если результат выборки вернул результат None выполняется SQL запрос на добавление записи.
        Если результат выборки вернул результат 2 (вернул кортеж размер которого равен двум).
        Вызывается исключение.
        
        param: 
            - user_login : str
            - user_password : str
        '''
        
        self.cur.execute(f"SELECT user_login, user_password FROM users WHERE user_login='{user_login}' and user_password='{user_password}'")

        if self.cur.fetchone() is None:
            self.cur.execute(f"INSERT INTO users (user_login, user_password) VALUES ('{user_login}','{user_password}')")
            self.conn.commit()
        elif len(self.cur.fetchone() == 2):
            raise
    
    def get_data_product(self):
        '''
        Служит для выборки всех записей из таблицы products. Выполняет SQL запрос на выборку
        
        return: list[tuple]
        '''
        
        self.cur.execute("SELECT * FROM products")
        data_product = self.cur.fetchall()
        return data_product

    def get_data_users(self): 
        '''
        Служит для выборки всех записей из таблицы users. Выполняет SQL запрос на выборку
        
        return: list[tuple]
        '''

        self.cur.execute("SELECT * FROM users")
        data_product = self.cur.fetchall()
        return data_product 
    
    def set_new_data_product(self, product_name: str, product_cost: str): 
        '''
        Служит для добавления записи в таблицу products. Выполняет SQL запрос на добавление
        
        param:
            - product_name: str
            - product_cost: str
        '''
        
        self.cur.execute(f"INSERT INTO products (product_name, product_cost) values ('{product_name}','{product_cost}')")
        self.conn.commit()
    
    def remove_data_product(self, product_id: int , product_name: str): 
        '''
        Служит для удаления записи из таблицы products. Выполняет SQL запрос на удаление
        
        param:
            - product_id: int
            - product_name: str
        return:
            int 
        '''
    
        self.cur.execute(f"DELETE FROM products WHERE product_id='{product_id}' AND product_name='{product_name}'")
        self.conn.commit()
        return self.cur.rowcount
    
    def get_data_deal(self, usr_login: str): 
        '''
        Служит для выборки из нескольких таблиц для заполнения таблицы (личный кабинет) в панели пользователя.
        Выполняет SQL запрос на выборку.
        
        param:
             - usr_login: str 
        return:
            list[tuple]
        '''

        self.cur.execute(f"""SELECT (us.user_login), (pr.product_name), (pr.product_cost), (tr.order_date) FROM products pr 
                         INNER JOIN transact tr ON (pr.product_id) = (tr.product_id) INNER JOIN users us ON (us.user_id) = (tr.customer_id) 
                         WHERE (us.user_login) = '{usr_login}'""")
        data_deals = self.cur.fetchall()
        return data_deals
    
    def set_data_deal(self, usr_login: str, product_name: str):
        '''
        Служит для добавление записи в таблицу transact. Выполняет SQL запрос на добавление
        
        param:
             - usr_login: str
             - product_name: str
        return:
            int
        
        '''    
        
        self.cur.execute(f"""INSERT INTO transact (customer_id, product_id, transaction_price) SELECT user_id, product_id, product_cost 
                         FROM users, products WHERE user_login='{usr_login}' AND product_name ='{product_name}'""")
        self.conn.commit()
        return self.cur.rowcount
    
    def set_data_user_balance_update(self, user_balance: str, user_login: str): 
        '''
        Служит для обновления записи в таблице users. Выполняет SQL запрос на обновление
        
        param:
             - user_balance: str
             - user_login: str
        return:
            int
        '''    
        
        self.cur.execute(f"UPDATE users SET user_balance='{float(user_balance)}' WHERE user_login='{user_login}'")
        self.conn.commit()
        return self.cur.rowcount
        
    def set_calculate_user_balance(self, usr_login: str): 
        '''
        Служит для обновления записи в таблице users. Выполняет SQL запрос на обновление
        
        param:
             - user_login: str
        '''    
        
        self.cur.execute(f"""UPDATE 
	                            users 
                            SET 
	                            user_balance = (SELECT us.user_balance - pr.product_cost
					            FROM products pr INNER JOIN transact tr ON (pr.product_id) = (tr.product_id) 
					            INNER JOIN users us ON (us.user_id) = (tr.customer_id) WHERE us.user_login = '{usr_login}' 
                                GROUP BY us.user_balance, pr.product_cost)
                            WHERE user_login = '{usr_login}'""")
        self.conn.commit()

    def set_current_balance(self, user_login: str):
        '''
        Служит для выборки user_balance из таблицы users. Выполняет SQL запрос на выборку
        
        param:
             - user_login: str
        '''
        
        self.cur.execute(f"SELECT user_balance FROM users WHERE user_login='{user_login}'")
        data = self.cur.fetchone()
        return data
    
    def get_close_connecetion(self):
        '''
        Служит для разрыва соединения с БД
        
        '''
        self.conn.close()    
        
