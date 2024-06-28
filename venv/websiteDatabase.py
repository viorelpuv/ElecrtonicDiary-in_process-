import sqlite3 as sql


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

    def select_user_with_login(self, login):
        return self.cur.execute("""SELECT Имя, Фамилия FROM telegram_users WHERE Логин = ?""",
                                (login,)).fetchone()

    def __del__(self):
        self.cur.close()
        self.con.close()