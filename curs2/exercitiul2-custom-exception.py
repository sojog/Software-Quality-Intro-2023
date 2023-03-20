
import re

class InvalidIdException(Exception):
    def __str__(self):
        return 'Id-ul trebuie sa fie un numar mai mare ca 100'

class NameException(Exception):
    def __str__(self):
        return 'Formatul numelui este incorect'

class EmailException(Exception):
    def __str__(self):
        return 'Formatul emailului este incorect'


class Utilizator:
    def __init__(self, id, prenume, nume, email):
        if id < 100: 
            raise InvalidIdException()
        self.id = id

        if not isinstance(prenume, str) or len(prenume) < 2 or not prenume.isalpha():
            raise NameException()
        self.prenume = prenume

        if any([not isinstance(nume, str), len(nume) < 2, not nume.isalpha()]):
            raise NameException()
        self.nume = nume

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not isinstance(email, str) or not re.fullmatch(regex, email):
            raise EmailException()
        self.email = email


    def __str__(self):
        return f'Utilizatorul {self.prenume} {self.nume}'


user1 = Utilizator(101, 'ion', 'pop', 'ion@pop.com')
print(user1)
user2 = Utilizator(102, 'maria', 'vasile', 'maria@vasile.com')
print(user2)

user3 = Utilizator(9797, 'alin', 'george', 'test@t.co')
print(user3)
