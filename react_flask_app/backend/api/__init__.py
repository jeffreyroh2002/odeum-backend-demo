from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect  # Import CSRFProtect
from react_flask_app.backend.api.config import Config
import os
from flask_cors import CORS

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()

# Initialize CSRFProtect
csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    CORS(app)
    
    # Initialize CSRFProtect with the Flask app instance
    csrf.init_app(app)

    # section for importing blueprints
    from react_flask_app.backend.api.main.routes import main
    from react_flask_app.backend.api.users.routes import users
    from react_flask_app.backend.api.tests.routes import tests
    from react_flask_app.backend.api.questions.routes import questions
    from react_flask_app.backend.api.results.routes import results
    from react_flask_app.backend.api.spotify.routes import spotify
    from react_flask_app.backend.api.presurvey.routes import presurvey
    
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(tests)
    app.register_blueprint(questions)
    app.register_blueprint(results)
    app.register_blueprint(spotify)
    app.register_blueprint(presurvey)

    return app