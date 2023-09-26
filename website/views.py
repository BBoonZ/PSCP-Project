from flask import Blueprint, render_template
from flask_login import logout_user, current_user


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('base.html')

@views.route('/test')
def test():
    return render_template('test.html')