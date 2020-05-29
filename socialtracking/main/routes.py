from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from socialtracking.models import User, Post
from socialtracking.posts.forms import SearchBar
from flask_login import login_user, current_user, login_required

main = Blueprint('main', __name__)

@main.route('/homepage', methods=['GET', 'POST']) #The homepage where users can see all of the entries that they have created.
@login_required
def homepage():
    form = SearchBar()
    if form.validate_on_submit():
        search = form.search_field.data
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter_by(person_met = search, author=current_user).paginate(page=page, per_page=4)
        if posts == 0:
            flash('There were no results', 'danger')
        page = request.args.get('page', 1, type=int)
        return render_template('homepage.html', posts=posts, form=form)
    else:
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter_by(author=current_user).order_by(Post.date_met.desc()).paginate(page=page, per_page=4) #Only display the entries that the user has created on their homepage.
        return render_template('homepage.html', posts=posts, form=form)