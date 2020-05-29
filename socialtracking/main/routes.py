from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from socialtracking.models import User, Post
from socialtracking.posts.forms import SearchBar
from flask_login import login_user, current_user, login_required

main = Blueprint('main', __name__)

@main.route('/homepage', methods=['GET', 'POST']) #The homepage where users can see all of the entries that they have created.
@login_required
def homepage():
    form = SearchBar() #Form that has the elements for the search bar
    if form.validate_on_submit(): #If the search bar button is clicked then:
        search = form.search_field.data #Get what the value in the text field is
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter_by(person_met = search, author=current_user).paginate(page=page, per_page=4)#Paginate the results of the filter with a max of 
        if posts == 0:   #Could not figure out how to work but the logic is there                             #4 posts per page.
            flash('There were no results', 'danger')
        page = request.args.get('page', 1, type=int)
        return render_template('homepage.html', posts=posts, form=form)
    else:
        page = request.args.get('page', 1, type=int) #If the search bar is not activated simply serve all of the entries created by the user
        posts = Post.query.filter_by(author=current_user).order_by(Post.date_met.desc()).paginate(page=page, per_page=4)
        return render_template('homepage.html', posts=posts, form=form)