from enum import Enum

class Profesionisti:
    Ion = ('Ion', 'Pop', 'Project Manager')
    John = ('John', 'Doe', 'Designer')
    Maria = ('Maria', 'Popa', 'HR')
    Ilie = ('Ilie', '', 'Tester')


p1 = Profesionisti.Ion
p2 = Profesionisti.Maria

print(p1[-1])

