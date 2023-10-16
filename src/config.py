from decouple import config

class config:
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(config):
    DEBUG = True

class ProductionConfig(config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}