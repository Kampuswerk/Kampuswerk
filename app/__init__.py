"""
The flask application package.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import app_config


import os

db = SQLAlchemy()
login_manager = LoginManager();
login_manager.login_message = u" Use your favourite social media ID's to login & create a free account! "



def create_app(config_name):
    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.from_object(app_config[config_name])
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI'),
            OAUTH_CREDENTIALS_GOOGLE_ID=os.getenv('OAUTH_CREDENTIALS_GOOGLE_ID'),
            OAUTH_CREDENTIALS_GOOGLE_SECRET=os.getenv('OAUTH_CREDENTIALS_GOOGLE_SECRET'),
            OAUTH_CREDENTIALS_FACEBOOK_ID=os.getenv('OAUTH_CREDENTIALS_FACEBOOK_ID'),
            OAUTH_CREDENTIALS_FACEBOOK_SECRET=os.getenv('OAUTH_CREDENTIALS_FACEBOOK_SECRET'),
            OAUTH_CREDENTIALS_TWITTER_ID=os.getenv('OAUTH_CREDENTIALS_TWITTER_ID'),
            OAUTH_CREDENTIALS_TWITTER_SECRET=os.getenv('OAUTH_CREDENTIALS_TWITTER_SECRET')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py', silent=True)



    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = ".index"



    migrate = Migrate(app, db)

    from app import models

    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    return app
