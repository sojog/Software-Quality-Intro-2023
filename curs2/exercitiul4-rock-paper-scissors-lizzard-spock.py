from enum import Enum
from random import randint

class Joc(Enum):
    Piatra   = 1
    Foarfece = 2
    Hartie   = 3
    Spock    = 4
    Soparla  = 5 


while True:
    calculator = Joc(randint(1, 5))
    alegere = int(input('''Alegeti 
        1 - piatra
        2 - foarfece
        3 - hartie
        4 - spock
        5 - soparla
        '''))

    jucator = Joc(alegere)
    print('Ai ales', jucator)
    print('Calculatorul a ales', calculator)

    

    if jucator == calculator:
        print('Egalitate')
    else:
        if jucator == Joc.Piatra:
            if calculator == Joc.Foarfece or calculator == Joc.Soparla:
                print('Ai castigat')
            else:
                print('Ai pierdut')

        if jucator == Joc.Foarfece:
            if calculator == Joc.Hartie or calculator == Joc.Soparla:
                print('Ai castigat')
            else:
                print('Ai pierdut')

        if jucator == Joc.Hartie:
            if calculator == Joc.Piatra or calculator == Joc.Spock:
                print('Ai castigat')
            else:
                print('Ai pierdut')


        if jucator == Joc.Spock:
            if calculator == Joc.Foarfece or calculator == Joc.Piatra:
                print('Ai castigat')
            else:
                print('Ai pierdut')

        
        if jucator == Joc.Soparla:
            if calculator == Joc.Hartie or calculator == Joc.Spock:
                print('Ai castigat')
            else:
                print('Ai pierdut')

                