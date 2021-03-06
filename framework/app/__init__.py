"""
    Imports
"""
import sys

from flask import Flask
from flask_mongoengine import MongoEngine

from mongoengine import connect, MongoEngineConnectionError

DB = MongoEngine()

def create_app(**config_overrides):
    """
    Creates a flask application with the desired configuration settings
    and connects it to the database.
    """
    app = Flask(__name__)
    app.config.from_object('app.config')
    app.config['MONGODB_SETTINGS'] = {'db': 'evf_db'}

    from app.api import API
    app.register_blueprint(API)

    from app.ui import UI
    app.register_blueprint(UI)

    app.config.update(config_overrides)
    try:
        DB.init_app(app)
    except MongoEngineConnectionError as conn_err:
        print(conn_err)
        sys.exit('Could not connect to database.')

    return app

