from flask import Blueprint ,render_template, request, flash, redirect, url_for
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db
import datetime


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.login'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login2.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be grater than 3 characters', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least than 7 characters', category='error')
        else:
            # add user to database
            new_user = User(email=email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash('Account have been create', category='success')
            return redirect(url_for('auth.sign_up'))
    return render_template('sign-up.html', user=current_user)

@auth.route('/forgot', methods=['GET', 'POST'])
def forgot():
    return render_template('forgot.html', user=current_user)

@auth.route('/create-new-password', methods=['GET', 'POST'])
def newpass():
    return render_template('newpass.html', user=current_user)


@auth.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    if request.method == 'POST':
        note = request.form.get('text')
        print(note)
        current_datetime = datetime.datetime.today()

        month_name = current_datetime.strftime('%B')
        day_name = current_datetime.strftime('%A')

        _txt = Note(data=note, day=day_name, month=month_name, love='True', user_id=current_user.id)
        db.session.add(_txt)
        db.session.commit()

        flash('Your Diary has been Create!', category='success')
    return render_template('edit.html', user=current_user)
    