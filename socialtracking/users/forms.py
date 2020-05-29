from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from socialtracking.models import User

class RegistrationForm(FlaskForm): #Forms realted to the user
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordconfirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username ): #Making sure that the username is not already taken
        user = User.query.filter_by(username=username.data).first()
        if user: #If taken tell the user that the username is already taken
            raise ValidationError('That username is already taken.')

class LoginForm(FlaskForm): #Form for the log in page
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)]) #Information about the criteria for a username
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')#Button for the login