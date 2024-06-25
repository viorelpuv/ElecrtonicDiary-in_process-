import bcrypt


# #~#~#~# [ ШИФРАТОР ] #~#~#~#
class Hashing:
    def __init__(self, password):
        self.password = password
        self.salt = bcrypt.gensalt()

    def Encoding(self):
        return bcrypt.hashpw(self.password.encode(), self.salt).strip().decode('UTF-8')
