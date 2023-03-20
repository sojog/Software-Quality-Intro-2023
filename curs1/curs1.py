import random
import math
import requests
from altfolder import modululmeu


class Calculator:

    def suma(self, a, b):
        return a + b

    def diferenta(self, a, b):
        return a - b


def altceva():
    return 'yeah'

obj = modululmeu.MyClass()
# Poate fi apelata din exterior
obj.functia_publica()

# Astea nu trebuie sa fie apelata -  conventie
obj._functia_interna()
# Astea nu trebuie sa fie apelata -  conventie (NAME MANGLING)
obj._MyClass__functie_privata()


obj_mostenit = modululmeu.ClasaDerivata()
obj_mostenit.functia_publica()
obj_mostenit._functia_interna()
obj_mostenit._MyClass__functie_privata()

modululmeu.MyClass.__init__()



