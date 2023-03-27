from enum import Enum
from random import randint
import os

class Joc(Enum):
    Piatra = 1
    Hartie = 2
    Foarfeca = 3
    Soparla = 4
    Spock = 5

REGULI = {
    Joc.Foarfeca : (Joc.Hartie, Joc.Soparla),
    Joc.Piatra : (Joc.Foarfeca, Joc.Soparla ),
    Joc.Hartie : (Joc.Piatra, Joc.Spock) ,
    Joc.Soparla : (Joc.Spock , Joc.Hartie),
    Joc.Spock : (Joc.Piatra, Joc.Foarfeca) 
}

SCOR = {
    "om":0,
    "calculator": 0
}

def joaca(valoare_aleasa):
    om = Joc(valoare_aleasa)
    calculator = Joc(randint(1, 3))
    if om == calculator:
        print("Remiza")
    elif  calculator in REGULI[om]:
        print("Ai castigat")
        SCOR["om"] += 1
    else:
        print("Ai pierdut")
        SCOR["calculator"] += 1
    os.system("clear") # "cls" pe Windows
    print('Ai ales', om.name, 'Calculatorul a ales', calculator.name)
    print('Scorul este de ', SCOR["om"], "-", SCOR["calculator"])


while True:
    valoare_introdusa =  int(input("Introduceti valoare\n 1 - Piatra\n 2- Hartie\n 3 - Foarfeca\n 4- Sporala \n 5 - Spock \n"))
    joaca(valoare_introdusa)




