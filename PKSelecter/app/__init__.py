"""
Application Factory Module
"""
from logging import DEBUG, debug
from flask import Flask

from .api.views_api import views_bp
from .api.controller_api import controller_bp


def create_app(config):

    application = Flask(
        import_name=__name__, static_folder="./static/", template_folder="./static/"
    )

    application.config.from_object(config)

    application.register_blueprint(views_bp, url_prefix="/")
    application.register_blueprint(controller_bp, url_prefix="/")

    return application
