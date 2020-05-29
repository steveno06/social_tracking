from datetime import datetime
from socialtracking import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader #Work in progress, checks which users are currently logged in.
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin): #Structure of the database for the users
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "User('{}')".format(self.username)

class Post(db.Model): #Structure of the database for the posts/entries that each user makes
     id = db.Column(db.Integer, primary_key=True)
     person_met = db.Column(db.String(100), nullable=False)
     date_met = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
     content = db.Column(db.Text, nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #Each post has one author

     def __repr__(self):
         return "Post('{}', '{}', '{}')".format(self.person_met, self.date_met, self.content)

