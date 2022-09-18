import configparser
import psycopg2

config = configparser.ConfigParser()
config.read('config.ini')

# абстракция над postgressql  

class DataBase():
    
    def set_connect(self): # нужно закрыть 
        self.conn = psycopg2.connect(
            database=config['database']['dbname'],
            user=config['database']['user'],
            password=config['database']['password'],
            host=config['database']['host'],
            port=config['database']['port']
        )

        self.cur = self.conn.cursor()

    def set_authorisation(self, user_login, user_password):
        data = self.cur.execute(
            f"SELECT user_login, user_password, user_role_admin FROM users WHERE user_login='{user_login}' and user_password='{user_password}'") 

        data = self.cur.fetchone()
        return data
    
    def set_registration(self, user_login, user_password):
        self.cur.execute(f"SELECT user_login FROM users WHERE user_login='{user_login}'")
     
        if self.cur.fetchone() is None:
            self.cur.execute(f"INSERT INTO users (user_login, user_password) VALUES ('{user_login}','{user_password}')")
            self.conn.commit()
    
    def get_data_product(self):
        self.cur.execute("SELECT * FROM products")
        data_product = self.cur.fetchall()
        return data_product

    def get_data_users(self): 
        self.cur.execute("SELECT * FROM users")
        data_product = self.cur.fetchall()
        return data_product 
    
    def set_new_data_product(self, product_name, product_cost): 
        self.cur.execute(f"INSERT INTO products (product_name, product_cost) values ('{product_name}','{product_cost}')")
        self.conn.commit()
    
    def remove_data_product(self, product_id, product_name): 
        self.cur.execute(f"DELETE FROM products WHERE product_id='{product_id}' AND product_name='{product_name}'")
        self.conn.commit()
    
    def get_data_deal(self, usr_login): 
        self.cur.execute(f"SELECT (us.user_login), (pr.product_name), (pr.product_cost), (tr.order_date) FROM products pr INNER JOIN transact tr ON (pr.product_id) = (tr.product_id) INNER JOIN users us ON (us.user_id) = (tr.customer_id) WHERE (us.user_login) = '{usr_login}'")
        data_deals = self.cur.fetchall()
        return data_deals
    
    def set_data_deal(self, usr_login, product_name):
        self.cur.execute(f"INSERT INTO transact (customer_id, product_id) SELECT user_id, product_id FROM users, products WHERE user_login='{usr_login}' AND product_name = '{product_name}'")
        self.conn.commit()
    
    def set_data_user_balance_update(self, user_balance, user_login): 
        self.cur.execute(f"UPDATE users SET user_balance='{float(user_balance)}' WHERE user_login='{user_login}'")
        self.conn.commit()
    
    def set_calculate_user_balance(self, user_login): 
        self.cur.execute(f"SELECT us.user_balance - sum(pr.product_cost) FROM products pr INNER JOIN transact tr ON (pr.product_id) = (tr.product_id) INNER JOIN users us ON (us.user_id) = (tr.customer_id) WHERE (us.user_login) = '{user_login}' GROUP BY us.user_balance")
        data = self.cur.fetchone()
        return data 
        
    def set_current_balance(self, user_login):
        self.cur.execute(f"SELECT user_balance FROM users WHERE user_login='{user_login}'")
        data = self.cur.fetchone()
        return data
            
        
