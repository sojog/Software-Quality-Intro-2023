


def functie22():
    return 22

def decorator(func):
    print('decoratorul a fost chemat')
    return functie22

@decorator
def functie10():
    return 10

print(functie10())


