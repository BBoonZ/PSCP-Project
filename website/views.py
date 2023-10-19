from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('base.html', user=current_user)

@views.route('/home')
def home2():
    return render_template('navbar.html', user=current_user)

@views.route('/test2')
def test2():
    return render_template('test2.html', user=current_user)

@views.route('/test')
@login_required
def test():
    return render_template('test.html', user=current_user)

@views.route('add-db')
def add_db():

    return render_template('test3.html', user=current_user)
