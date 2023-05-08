class Config:
    SECRET_KEY = 'PROYECTO2_BD'

class DevelopmentConfig(Config):
    DEBUG = True
    PGSQL_HOST = 'localhost'
    PGSQL_USER = 'postgres'
    PGSQL_PASSWORD = 'Lind@1155'
    PGSQL_DATABASE = 'proyecto2'

config = {
    'development': DevelopmentConfig
}