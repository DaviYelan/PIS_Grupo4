class ConfigBD:
    SECRET_KEY = 'cevicheperuano'

class DevelopmentConfig(ConfigBD):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'shifusql'
    MYSQL_DB = 'PIS'

config = { 
    'development': DevelopmentConfig
}