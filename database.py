from mysql.connector import connect
from bot.handlers.hashing import Encryptor


class Database:
    def __init__(self):
        self.con = connect(
            host='localhost',
            user='',
            password=''
        )
        self.cur = self.con.cursor()
        self.cur.execute("""use data""")

    def add_user(self, user_id, username):
        self.cur.execute("""INSERT INTO telegram_users (user_id, username) VALUES (%s, %s)""",
                         (user_id, username))
        self.con.commit()

    def select_users(self, user_id):
        self.cur.execute("""SELECT * FROM telegram_users WHERE user_id = %s;""", (user_id,))
        return self.cur.fetchall()

    def select_usernames(self, login):
        self.cur.execute("""SELECT * FROM telegram_users WHERE Логин = %s""", (login,))
        return self.cur.fetchall()

    def __del__(self):
        self.cur.close()
        self.con.close()
