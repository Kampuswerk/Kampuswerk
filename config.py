"""Kampuswerk configuration
"""
import os

class Config(object):
    """Common settings.
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-really-need-to-change-this'
    SQLALCHEMY_POOL_RECYCLE = 499
    SQLALCHEMY_POOL_TIMEOUT = 20

class DevelopmentConfig(Config):
    """Development (local) environment specific settings.
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://development.db'

class StagingConfig(Config):
    """Pre-production specific settings.
    """
    DEBUG = True

class ProductionConfig(Config):
    """Production specific settings.
    """
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
