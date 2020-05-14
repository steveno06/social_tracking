from flask import render_template, url_for, flash, redirect, abort
from socialtracking import app, db, bcrypt
from socialtracking.forms import RegistrationForm, LoginForm, PostForm
from socialtracking.models import User, Post
from flask_login import login_user, current_user, logout_user


@app.route('/', methods=['GET', 'POST'])
def home():                                     #First thing user sees AKA home, but also acts like the login page to site.
    if current_user.is_authenticated:
        redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('homepage'))
        else:
            flash('Login unsuccessful. Check your username and password', 'danger')
    return render_template('home.html', form=form)

@app.route('/register', methods=['GET', 'POST']) #Users can register for an account
def register():
    if current_user.is_authenticated: #Check if a user is already logged in
        redirect(url_for('homepage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #Encrypt the password so that its not plain text in database
        user = User(username=form.username.data, password=hashed_password) #Create user with hashed password
        db.session.add(user)
        db.session.commit() #Add to the database
        flash('The account has been created, you may now log in', 'success')
        return redirect(url_for('homepage'))    #Redirect user to the homepage
    return render_template('register.html', form=form)

@app.route('/homepage', methods=['GET', 'POST']) #The homepage where users can see all of the entries that they have created.
def homepage():
    posts = Post.query.filter_by(author=current_user) #Only display the entries that the user has created on their homepage.
    return render_template('homepage.html', posts=posts)

@app.route("/logout") #Work in progress to logout users when they are done.
def logout():
    logout_user()
    redirect(url_for('homepage'))

@app.route('/homepage/create', methods=['GET', 'POST']) #Page where user creates a new entry to be added in the database.
def new_post():
    form= PostForm()
    if form.validate_on_submit():
        post = Post(location=form.name_title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Log has been saved!', 'success')
        return redirect(url_for('homepage'))
    return render_template("create_post.html", form=form)


@app.route('/homepage/<int:post_id>')
def log(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:             #make sure that only the owner can access the tracker, dont allow access to ther peoples trackers
        abort(403)
    else:
        return render_template('log.html', title=post.location, post=post)
