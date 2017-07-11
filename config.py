"""Kampuswerk configuration
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

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
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'kampuswerk-dev.sqlite')

class TestingConfig(Config):
    """Development (local) environment specific settings.
    """
    TESTING = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'kampuswerk-test.sqlite')

class StagingConfig(Config):
    """Pre-production specific settings.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('STAGE_DATABASE_URL')

class ProductionConfig(Config):
    """Production specific settings.
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

app_config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
