import os

from flask import Flask, render_template, request, redirect, flash, make_response
from websiteDatabase import Database

from bot.handlers.hashing import Encryptor

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/login', methods=['POST', 'GET'])
def login():
    db = Database()
    e = Encryptor()
    if request.method == 'POST':
        login_form = request.form['fnl']
        group_form = request.form['group']
        password_form = request.form['password']

        login_base = db.select_with_login(login=login_form, group=group_form, password=e.Encrypted(password_form))

        if len(login_form) != 0 and len(group_form) != 0 and len(password_form) != 0:
            if login_base:
                flash('Good!', 'message')
                print(login_form, group_form, password_form)
                return redirect(f'/main/{login_form}')
            else:
                flash('Bad!', 'message')
                return redirect('/')
        else:
            return "Пустое значение"
    else:
        return render_template('login.html')


@app.route('/main/<username>', methods=['POST', 'GET'])
def main(username):
    db = Database()
    username = db.select_user_with_login(login=username)
    user = {
        'username': f"{username[0] + ' ' + username[1]}"
    }
    return render_template('main.html', user=user)


@app.route('/test/<username>')
def cookie(username):
    return username


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
