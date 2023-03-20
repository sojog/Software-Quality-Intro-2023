
while True:

    a = input('Introduceti primul numar\n')
    b = input('Introduceti al doilea numar\n')
    try:
        # a sa nu fie transformat in int
        a = int(a)
        # b sa nu fie transformat in int
        b = int(b)
        # b = 0
        rezultat = a / b
    except ValueError:
        print('A exista o eroare de tipul Value Error')
    except ZeroDivisionError:
        print('Impartirea la 0 nu are sens')
    except:
        print('A exista o eroare generala')
    else:
        print('Ramura else este executata - in caz de nu e eroare')
    finally:
        print('Ramura finally este executata in orice caz')
    
# print(rezultat)


