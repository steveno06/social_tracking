from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from socialtracking import db, bcrypt
from socialtracking.models import User, Post
from socialtracking.users.forms import RegistrationForm, LoginForm
from socialtracking.users.middleware import loggedIn_middleware

users = Blueprint('users', __name__)

def hash_password(form):
    return bcrypt.generate_password_hash(form.password.data).decode('utf-8')

def commit_fields_to_database(form, hashed_password):
        user = User(username=form.username.data, password=hashed_password) 
        db.session.add(user)
        db.session.commit()

def logged_in(current_user):
    if current_user.is_authenticated: 
        return True

def is_a_user(user, form):
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        return True


@users.route('/', methods=['GET', 'POST'])
@loggedIn_middleware
def home():                                     #First thing user sees AKA home, but also acts like the login page to site.
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if is_a_user(user, form):
            return redirect(url_for('main.homepage'))
        else:
            flash('Login unsuccessful. Check your username and password', 'danger')
    
    return render_template('home.html', form=form)

@users.route('/register', methods=['GET', 'POST']) #Users can register for an account
@loggedIn_middleware
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        hashed_password = hash_password(form)
        commit_fields_to_database(form, hashed_password)
        flash('The account has been created, you may now log in', 'success')
        return redirect(url_for('main.homepage'))  
    
    return render_template('register.html', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('users.home'))


