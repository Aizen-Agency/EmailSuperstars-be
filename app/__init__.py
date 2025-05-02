# app/__init__.py
import os
from flask import Flask
from flask_mail import Mail
from flask_cors import CORS
from .routes.home import home
from .routes.contact import contact

mail = Mail()  # Only here!

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object('app.config.Config')

    mail.init_app(app)

    app.register_blueprint(home)
    app.register_blueprint(contact, url_prefix="/api")

    return app
# 