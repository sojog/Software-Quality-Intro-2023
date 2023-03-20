


def inlocuieste_functia(func):
    def suma_patratelor(a, b):
        return a ** 2 + b ** 2
    return suma_patratelor




@inlocuieste_functia
def adunare(a, b):
    return a + b

print(adunare(2, 3))