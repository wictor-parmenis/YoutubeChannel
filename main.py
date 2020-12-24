import sqlite3
import random
import string
from tkinter import *

class Password:

    password = []
    letters = string.ascii_lowercase
    new_pwd = ''

    def __init__(self, number_char, context):
        self._number_char = int(number_char)
        self._context = context

    def add_password(self):
        # Falta gerar condicional para caso o number_char seja par ou ímpar.
        for i in range(self._number_char):
            if i % 2 == 0:
                self.password.append(random.choice(self.letters))
            elif i % 2 == 1:
                self.password.append(random.randint(0, 9))  
        #self.password = str(self.password)  
        print(f'Password with {self._number_char} characters for {self._context}: ', end='')    
        for text in self.password:
            print(f'{text}', end='')
        
class GUI:
    


if __name__ == '__main__':

    a1 = Password(11, 'instagram')
    a1.add_password()

