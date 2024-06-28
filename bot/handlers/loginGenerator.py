from random import choice
from bot.utils.database import Database


class LoginGenerate:
    def __init__(self, s_name, f_name, l_group):
        self.fio = [s_name, f_name, f"{l_group}".split('-')[1]]
        self.db = Database()
        self.generating_logins = []
        self.symbols = ['/', '-', '!', '@', '#', '$']

    def generate(self):
        login = self.fio[1][0] + self.fio[0] + self.fio[2]
        symbols = choice(self.symbols)
        if self.db.select_usernames(login):
            while self.db.select_usernames(self.generating_logins):
                return f"{login}" + f"{symbols}"
        else:
            return login
