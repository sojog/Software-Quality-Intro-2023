while True:
    x = input('Introduceti pe x\n')
    try:
        x = int(x)
    except ValueError as identifier:
        print('x trebuie sa fie numar')
        continue


    y = input('Introduceti pe y\n')
    try:
        y = int(y)
    except ValueError as identifier:
        print('y trebuie sa fie numar')
        continue


    suma = x + y
    print('suma = ', suma)


