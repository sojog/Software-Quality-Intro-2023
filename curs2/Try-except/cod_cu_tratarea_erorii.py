from cod_cu_posibila_eroare import verifica

while True:
    x = int(input("Introduceti pe x de la tastatura\n"))
    try:
        verifica(x)
    except:
        print('Trebuie integer pozitiv')