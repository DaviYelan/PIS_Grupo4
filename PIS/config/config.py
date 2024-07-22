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
    ORACLE_HOST = 'localhost'
    ORACLE_PORT = '1521'
    ORACLE_SID = 'xe'
    ORACLE_USER = 'PIS'
    ORACLE_PASSWORD = 'Kenichi04'
    ORACLE_DB = 'PIS'

config = {
    'development': DevelopmentConfig
}