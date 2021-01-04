import os


class Config(object):
    DEBUG = False
    TESTING = False
    TELEGRAM_WEBHOOK_KEY = os.environ.get("TELEGRAM_WEBHOOK_KEY")


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    TELEGRAM_WEBHOOK_KEY = ""
