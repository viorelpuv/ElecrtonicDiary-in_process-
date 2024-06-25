from googletrans import Translator


class LoginGenerate:
    def __init__(self, s_name, f_name, l_group):
        self.fio = [s_name, f_name, f"{l_group}".split('-')[1]]

    def generate(self):
        return self.fio[1][0] + self.fio[0] + self.fio[2]
