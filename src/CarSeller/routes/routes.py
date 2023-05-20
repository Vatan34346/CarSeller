from src.helpers.authhelper import AuthHandler
from flask import Blueprint, request, render_template,redirect

main = Blueprint('main', __name__)


@main.route('/login', methods=["POST", "GET"])
def auth():
    if request.method == 'POST':
        auth_user = AuthHandler(request.form['username'], request.form['password'])
        logged = auth_user.login()
        if logged == 'User exists':
            return redirect('/home')

    return render_template('authenticate.html')


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')
