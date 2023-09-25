from flask import Blueprint ,render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login2.html')

@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        print('true')
    return render_template('sign-up.html')