
# #~#~#~# [ ШИФРАТОР ] #~#~#~#
class Encryptor:
    def __init__(self):
        self.encrypted_word = []

    def Encrypted(self, password):
        for i in password:
            self.encrypted_word.append(i)
        step_1 = ''.join(self.encrypted_word[::-1])
        step_2 = bin(int.from_bytes(step_1.encode('utf-8', 'surrogatepass'), 'big'))[2:]
        step_3 = step_2.zfill(8 * ((len(step_2) + 7) // 8))
        step_4 = step_3.replace('1', 'ペニス')
        step_5 = step_4.replace('0', 'はい')
        self.encrypted_word.clear()
        return step_5

    def Decrypted(self, encrypted_code):
        step_1 = f"{encrypted_code}".replace('はい', '0')
        step_2 = step_1.replace('ペニス', '1')
        step_3 = int(step_2, 2)
        step_4 = (step_3.to_bytes((step_3.bit_length() + 7) // 8, 'big')
                  .decode('utf-8', 'surrogatepass') or '\0')
        for i in step_4:
            self.encrypted_word.append(i)
        step_5 = ''.join(self.encrypted_word[::-1])
        return step_5
