class Config:
    SECRET_KEY = 'cevicheperuano'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root123'
    MYSQL_DB = 'cuenta'

config = { 
    'development': DevelopmentConfig          
}