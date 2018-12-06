from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():

    user = {'username': 'et'}

    posts = [
        {
            'author': {'username': 'J-Dub'},
            'body': 'Great sunday spent programming',
            'tags': ['coding', 'flask']
        },
        {
            'author': {'username': 'X-box'}, 
            'body': 'Is car sickness genetically inherited',
            'tags': ['life', 'worries']
        }
    ]
    
    return render_template('index.html', 
                            title='Flask Mega', 
                            posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():

    # Already authenticatd (handles situation when user manually returns to login page)
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # Not authenticated yet
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        # User now validated
        login_user(user, remember=form.remember_me.data) 
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign in', form=form)
   
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()

    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]

    return render_template('user.html', user=user, posts=posts)