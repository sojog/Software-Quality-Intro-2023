
#####  Entitate A  ####
class AgeTypeError(Exception):
    def __str__(self):
        return "Varsta trebuie sa fie int"

class NegativeAgeError(Exception):
    def __str__(self):
        return "Varsta trebuie sa fie mai mare ca 0"


# documentare COMMAND + SHIFT + 2
def este_major(varsta):
    """ O functie care intoarce daca este major

    Args:
        varsta (int): [description]

    Raises:
        AgeTypeError: atunci cand varsta introdusa nu este int
        NegativeAgeError: atunci cand varsta introdusa este mai mica decat 0

    Returns:
        bool: comparatie cu 18
    """    
    if not isinstance(varsta, int):
        raise AgeTypeError()
    if varsta < 0:
        raise NegativeAgeError()

    return varsta >= 18

#####  Entitate B  ####



try:
    
    print(este_major(19))
    print(este_major({}))
    print(este_major(7))
    

except AgeTypeError as identifier:
    print('Am prins o eroare de tipul AgeTypeError')
except NegativeAgeError as identifier:
    print('Am prins o eroare de tipul NegativeAgeError')








