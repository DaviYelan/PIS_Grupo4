from os import environ, path
from dotenv import load_dotenv


base_dir = path.abspath(path.dirname('__file'))
load_dotenv(path.join(base_dir, 'config/.env'))

class Config:

#Configuracion general
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = 'cevicheperuano'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root123'
    MYSQL_DB = 'pis'

config = { 
    'development': DevelopmentConfig
}