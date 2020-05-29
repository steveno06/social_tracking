from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from socialtracking.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.home'
login_manager.login_message_category = 'info'



def create_app(config_class=Config):
    app = Flask(__name__)                                         #set up for the whole application, setting up the database connection
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from socialtracking.users.routes import users
    from socialtracking.posts.routes import posts
    from socialtracking.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app