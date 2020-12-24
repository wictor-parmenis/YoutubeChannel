import sqlite3
import random
import string

class Password:

    password = []
    letters = string.ascii_lowercase

    def __init__(self, number_char, context):
        self._number_char = int(number_char / 2)
        self._context = context

    def add_password(self):
        # Falta gerar condicional para caso o number_char seja par ou ímpar.
        for i in range(self._number_char):
            self.password.append(random.choice(self.letters))
            self.password.append(random.randint(0, 9))
        return print(self.password)



if __name__ == '__main__':

    a1 = Password(3, 'instagram')
    a1.add_password()

