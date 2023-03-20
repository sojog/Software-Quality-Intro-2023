
""" Problema: Comparatia stringurilor """

country = 'ROmania'
if country == 'R0mania':
    print('esti in tara ta')



""" Solutia: Folosirea enumerarilor"""
import enum

class Tari(enum.Enum):
    RO = 'Romania'
    BG = 'Bulgaria'
    D  = 'Germany'

country = Tari.RO

if country == Tari.D:
    print('Sunt la fel')





