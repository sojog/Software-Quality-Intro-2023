from enum import Enum

class Zodii(Enum):
    Berbec  = 1
    Taur    = 2
    Gemeni  = 3
    Rac     = 4

persoana1 = Zodii.Taur
persoana2 = Zodii.Rac

if (persoana1 == persoana2):
    print('Au aceeasi zodie')
else:
    print('Nu au aceeasi zodie')



print('Persoana 1 are valoare', persoana1.value, persoana1.name)
print('Persoana 2 are valoare', persoana2.value, persoana2.name)

