
"""
Application Factory Module
"""
from flask import Flask
# from app.api.controller_api import controller_bp
from .api.views_api import views_bp


def create_app():
    app = Flask(__name__,
        static_folder='./templates/',
        template_folder='./templates/')
        
    app.register_blueprint(views_bp,  url_prefix='/')
    return app
