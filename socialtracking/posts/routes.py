from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, current_app
from socialtracking import db, bcrypt
from socialtracking.posts.forms import PostForm, SearchBar
from socialtracking.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = Blueprint('posts', __name__)

def check_author_access(post):
    if post.author != current_user:             #make sure that only the owner can access the tracker, dont allow access to ther peoples trackers
        abort(403)
        return False

def add_to_database(post):
    db.session.add(post)
    db.session.commit()

def update_database(post, form):
    post.person_met = form.name_title.data
    post.content = form.content.data
    db.session.commit()

def fill_text_fields(post, form):
    form.name_title.data = post.person_met
    form.content.data = post.content

def delete_in_database(post):
    db.session.delete(post)
    db.session.commit()

@posts.route('/homepage/create', methods=['GET', 'POST']) #Page where user creates a new entry to be added in the database.
@login_required
def new_post():
    form= PostForm()
    if form.validate_on_submit():
        post = Post(person_met=form.name_title.data, content=form.content.data, author=current_user)
        add_to_database(post)
        flash('Log has been saved!', 'success')
        return redirect(url_for('main.homepage'))
    return render_template("create_post.html", form=form)


@posts.route('/homepage/<int:post_id>') #Route for a specific post
@login_required
def log(post_id):
    post = Post.query.get_or_404(post_id)
    if check_author_access(post):
        pass
    else: 
        return render_template('log.html', title=post.person_met, post=post)


@posts.route("/homepage/<int:post_id>/update", methods=['GET', 'POST']) #Route to modify a post
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id) #Make sure the post exists
    check_author_access(post)
    form = PostForm()
    if form.validate_on_submit(): #When the button is click, retreive the new information and update the database
        update_database(post, form)
        flash('Your post has been updated!', 'success')
        return redirect(url_for('main.homepage', post_id=post.id))
    elif request.method == 'GET': #If not fill in the text fields with the information from the database
        fill_text_fields(post, form)
    return render_template('create_post.html', title='Update Post',
                           form=form)

    
@posts.route("/homepage/<int:post_id>/delete", methods=['POST']) #Route to delete the posts
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    check_author_access(post)
    delete_in_database(post)
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.homepage')) #After giving user feedback, redirect to homepage.
