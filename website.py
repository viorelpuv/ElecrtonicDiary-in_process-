import os
import sqlite3 as sql

from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)


class Database:
    def __init__(self):
        self.con = sql.connect('data.db')
        self.cur = self.con.cursor()

    def add_user(self, login, group, password):
        self.cur.execute("""INSERT INTO users(login, group_, password) VALUES (?, ?, ?)""",
                         (login, group, password))
        self.con.commit()

    def select_users(self):
        return self.cur.execute("""SELECT * FROM telegram_users""").fetchall()

    def select_with_login(self, login, group, password):
        return self.cur.execute("""SELECT * FROM telegram_users WHERE Логин = ? AND Группа = ? AND Пароль = ?""",
                                (login, group, password)).fetchone()

    def __del__(self):
        self.cur.close()
        self.con.close()


@app.route('/', methods=['POST', 'GET'])
@app.route('/login', methods=['POST', 'GET'])
def login():
    db = Database()
    if request.method == 'POST':
        login_form = request.form['fnl']
        group_form = request.form['group']
        password_form = request.form['password']

        login_base = db.select_with_login(login=login_form, group=group_form, password=password_form)

        if len(login_form) != 0 and len(group_form) != 0 and len(password_form) != 0:
            if login_base:
                flash('Good!', 'message')
                print(login_form, group_form, password_form)
                return redirect('/')
            else:
                flash('Bad!', 'message')
                return redirect('/')
        else:
            return "Пустое значение"
    else:
        return render_template('login.html')


@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
