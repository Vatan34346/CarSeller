from src.helpers.authhelper import AuthHandler
from flask import Blueprint, request, render_template,redirect
from src.Services.CopartService import CopartService

main = Blueprint('main', __name__)


@main.route('/', methods=["POST", "GET"])
def auth():
    if request.method == 'POST':
        auth_user = AuthHandler(request.form['username'], request.form['password'])
        logged = auth_user.login()
        if logged == 'User exists':
            return redirect('/home')

    return render_template('authenticate.html')


@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/go_to_copart')
def copart_site():
    copart = CopartService()
    copart.go_to_car_inventory()
    return 'success', 200
