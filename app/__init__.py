import os
from flask import Flask
from flask_mail import Mail
from .routes.home import home
from .routes.contact import contact
from .utils import mail
from flask_cors import CORS


mail = Mail()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object('app.config.Config')

    app.config.update(
        MAIL_SERVER = os.getenv('SMTP_HOST', 'smtp.gmail.com'),
        MAIL_PORT = os.getenv('SMTP_PORT', 587),
        MAIL_USE_TLS = True,
        MAIL_USERNAME = os.getenv('SMTP_USER'),
        MAIL_PASSWORD = os.getenv('SMTP_PASSWORD'),
        MAIL_DEFAULT_SENDER = os.getenv('SMTP_USER'),
    )

    mail.init_app(app)

    app.register_blueprint(home)

    app.register_blueprint(contact, url_prefix="/api")

    return app
