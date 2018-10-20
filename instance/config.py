import os
class Config():
    DEBUG = False
    TESTING = False
    CSRF_ENABLE = True
    SECRET_KEY = os.getenv('SECRET_KEY')

class Development(Config):
    DEBUG = True
    TESTING = True

configurations = {
    "production" : Config,
    "development" : Development
}