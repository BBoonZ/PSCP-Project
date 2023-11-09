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

@views.route('/history/<month>')
@login_required
def history(month):
    if month == 'none':
        val = Note.query.filter_by(user_id=current_user.id).all()
    else:
        val = Note.query.filter_by(user_id=current_user.id, month=month).all()
    val = val[::-1]
    val = [str(i) for i in val]
    return render_template('history.html', user=current_user, note=val, val=len(val))

@views.route('/history/diary/<note_id>')
@login_required
def history_2(note_id):
    note = Note.query.filter_by(user_id=current_user.id).all()
    note_str = [str(i) for i in note]
    note_date = [str(i.date).split()[0].split('-')[2] for i in note]
    for i in note:
        i = str(i.date).split()[0].split('-')[2]
        print(i)
    return render_template(
        'history_2.html',
        user=current_user,
        note_id=note_id, 
        note=note,
        note_len=len(note_str),
        note_str=note_str,
        note_date=note_date
    )

@views.route('/diary')
@login_required
def diary():
    val = Note.query.filter_by(user_id=current_user.id).all()
    val = val[::-1][0]
    val_date = str(val.date).split()[0].split('-')[2]
    val_month = val.month
    return render_template('diary.html', user=current_user, note=val, val_month=val_month, val_date=val_date)

'''@views.route('/test2/<note_id>')
@login_required
def test2(note_id):
    note = Note.query.filter_by(user_id=current_user.id).all()
    note_str = [str(i) for i in note]
    return render_template('test2.html', user=current_user, note_id=note_id, note=note, note_len=len(note_str), note_str=note_str)'''

@views.route('/test')
@login_required
def test():
    return render_template('test.html', user=current_user)

@views.route('add-db')
def add_db():

    return render_template('test3.html', user=current_user)
