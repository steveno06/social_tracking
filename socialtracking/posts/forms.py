from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class PostForm(FlaskForm):
    name_title = StringField('Name', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class SearchBar(FlaskForm):
    search_field = StringField('Search_Field', validators=[DataRequired()])
    submit= SubmitField('Search')