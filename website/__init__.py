from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer

db = SQLAlchemy()
DB_NAME = "database.db"

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'KdEadkoEE3lkWWoSlgoJO'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'  # เปลี่ยนเป็น SMTP server ของคุณ
    app.config['MAIL_PORT'] = 587  # ปรับเป็นพอร์ตของ SMTP server ของคุณ
    app.config['MAIL_USE_TLS'] = True  # ใช้ TLS (Transport Layer Security)
    app.config['MAIL_USE_SSL'] = False  # ไม่ใช้ SSL
    app.config['MAIL_USERNAME'] = 'titleman00123@gmail.com'  # ระบุชื่อผู้ใช้ SMTP server ของคุณ
    app.config['MAIL_PASSWORD'] = 'gtqg kibc otci tcvd'  # ระบุรหัสผ่าน SMTP server ของคุณ

    mail.init_app(app)
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

    app.serializer = serializer

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Create Database!')