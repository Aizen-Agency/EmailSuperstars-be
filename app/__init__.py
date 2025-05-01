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

    mail.init_app(app)

    app.register_blueprint(home)

    app.register_blueprint(contact, url_prefix="/api")

    return app
