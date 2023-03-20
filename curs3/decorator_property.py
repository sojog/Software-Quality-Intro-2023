
# __ -> private
# _ -> interna/protected
# fara -> publica

class Masina:
    def __init__(self, km, vechime=0):
        self.__km = km
        self.__vechime = vechime

    def __str__(self):
        return f'Masina are {self.__km} km'

    @property
    def km(self):
        return self.__km

    @km.setter
    def km(self, new_km):
        if new_km > 0 and new_km >  self.__km:
            self.__km = new_km

    
    @property
    def vechime(self):
        return self.__vechime


    # getter
    def getKm(self):
        return self.__km
    
    # setter
    def setKm(self, new_km):
        if new_km > 0 and new_km >  self.__km:
            self.__km = new_km


    # getter
    def getVechime(self):
        return self.__vechime

    # setter
    def setVechime(self, new_age):
        if new_age > 0 and new_age > self.__vechime:
            self.__vechime = new_age



dacia = Masina(100)
dacia.setKm(115)
dacia.setKm(-205)
print(dacia.getKm())

dacia.getKm()
print(dacia.km)
dacia.km = -100
print(dacia)


# print(dacia)

# bmw = Masina(200)
# print(bmw)

# print(bmw)

