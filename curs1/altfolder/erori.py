lista = []

while True:
    try:
        x = int(input('Introduceti numarul\n'))
    except:
        print('A exista o eroare')
    
    if x % 2 == 0:
        lista.append(x)
    else:
        raise ValueError('x este impar')
    print('Lista contine pe ', lista)





