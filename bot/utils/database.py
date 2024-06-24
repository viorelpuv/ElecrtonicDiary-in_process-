import sqlite3 as sql


class Database:
    def __init__(self):
        self.con = sql.connect(r'E:\Project\ElDiary\data.db')
        self.cur = self.con.cursor()

    def add_user(self, user_id, second_name, first_name, middle_name, group, password):
        self.cur.execute("""INSERT INTO telegram_users (user_id, Фамилия, Имя, Отчество, Группа, Пароль)
        VALUES (?, ?, ?, ?, ?, ?)""", (user_id, second_name, first_name, middle_name, group, password))
        self.con.commit()

    def select_users(self, user_id):
        return (self.cur.execute("""SELECT * FROM telegram_users WHERE user_id = ?""", (user_id,))
                .fetchall())

    def __del__(self):
        self.cur.close()
        self.con.close()

