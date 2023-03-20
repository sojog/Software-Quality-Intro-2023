from enum import Enum
from random import randint

class Joc(Enum):
    Piatra   = 1
    Foarfece = 2
    Hartie   = 3


while True:
    calculator = Joc(randint(1, 3))
    alegere = int(input('''Alegeti 
        1 - piatra
        2 - foarfece
        3 - hartie
        '''))

    jucator = Joc(alegere)
    print('Ai ales', jucator)
    print('Calculatorul a ales', calculator)

    if jucator == calculator:
        print('Egalitate')
    else:
        if jucator == Joc.Piatra:
            if calculator == Joc.Foarfece:
                print('Ai castigat')
            else:
                print('Ai pierdut')

        if jucator == Joc.Foarfece:
            if calculator == Joc.Hartie:
                print('Ai castigat')
            else:
                print('Ai pierdut')

        if jucator == Joc.Hartie:
            if calculator == Joc.Piatra:
                print('Ai castigat')
            else:
                print('Ai pierdut')


                