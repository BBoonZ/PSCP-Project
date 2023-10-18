from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('base.html', user=current_user)

@views.route('/home')
def home2():
    return render_template('navbar.html', user=current_user)

@views.route('/test2')
def test2():
    return render_template('history.html', user=current_user)

@views.route('/test')
@login_required
def test():
    return render_template('test.html', user=current_user)