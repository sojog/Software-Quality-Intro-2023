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
    alegere = int(input('''Alegeti 1..5
    '''))

    jucator = Joc(alegere)
    print('Ai ales', jucator)
    print('Calculatorul a ales', calculator)

    castigatoare = {
            Joc.Piatra:  (Joc.Foarfece, Joc.Soparla),
            Joc.Foarfece: (Joc.Hartie,  Joc.Soparla),
            Joc.Hartie: (Joc.Piatra, Joc.Spock),
            Joc.Spock: (Joc.Foarfece, Joc.Piatra),
            Joc.Soparla: (Joc.Hartie, Joc.Spock)
    }
    if jucator == calculator:
        print('Egalitate')
    else:
        if calculator in castigatoare[jucator]:
            print('Ai castigat')
        else:
            print('Ai pierdut')


