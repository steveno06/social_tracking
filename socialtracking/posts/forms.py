from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class PostForm(FlaskForm): #Forms related to the entries that are added to the database
    name_title = StringField('Who did you meet?', validators=[DataRequired()]) 
    content = TextAreaField('Details/Location', validators=[DataRequired()])
    submit = SubmitField('Post')

class SearchBar(FlaskForm):#Form for the search bar which is seen in the hopepage
    search_field = StringField('Search_Field', validators=[DataRequired()])
    submit= SubmitField('Search')