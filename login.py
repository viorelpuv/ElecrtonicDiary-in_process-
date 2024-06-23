import os
import sqlite3 as sql

import flask.typing
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
        return self.cur.execute("""SELECT * FROM users""").fetchall()

    def __del__(self):
        self.cur.close()
        self.con.close()


@app.route('/', methods=['POST', 'GET'])
def login_test():
    db = Database()
    if request.method != 'GET':
        login = request.form['fnl']
        group = request.form['group']
        password = request.form['password']

        users = db.select_users()

        if len(login) != 0 and len(group) != 0 and len(password) != 0:
            for user in users:
                if login == user[1] and group == user[2] and password == user[3]:
                    flash('Good!', 'message')
                    return redirect('/')
            else:
                flash('Bad!', 'message')
                return redirect('/')
        else:
            return "Пустое значение"
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
