from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import time

class Pic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    data = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    day = db.Column(db.String(50))
    month = db.Column(db.String(50))
    love = db.Column(db.String(50))
    filename = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    verification_token = db.Column(db.String(200), nullable=True)
    is_verified = db.Column(db.Boolean, default=False)
    notes = db.relationship('Note')
    pic = db.relationship('Pic')

