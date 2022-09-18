from configparser import ConfigParser

config = ConfigParser()


config['database'] = {
    "dbname" : 'shop_syn',
    "user" : 'postgres',
    "password" : 'hower19',
    "host" : 'localhost',
    "port": '5432'
}

with open('config.ini','w') as file:
    config.write(file)