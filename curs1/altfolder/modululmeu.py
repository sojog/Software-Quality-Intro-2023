class MyClass:
    # functie publica
    def functia_publica(self):
        print("Apelez public")

    def _functia_interna(self):
        print("Apelez intern")

    def __functie_privata(self):
        print("Apelez privat")


class ClasaDerivata(MyClass):
    pass