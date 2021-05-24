from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from socialtracking.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.home' #Show where users log in to the website.
login_manager.login_message_category = 'info'



def create_app(config_class=Config):  #set up for the whole application, setting up the database connection
    app = Flask(__name__)                                        
    app.config.from_object(Config) #Using the class created to retrieve and initialize the configuration.
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from socialtracking.users.routes import users #Extract
    from socialtracking.posts.routes import posts
    from socialtracking.main.routes import main

    app.register_blueprint(users)#Initialize the blueprints to be used through the project
    app.register_blueprint(posts)#Extract
    app.register_blueprint(main)

    return app