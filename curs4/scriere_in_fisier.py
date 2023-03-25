

# deschide fisierul pentru citire
f = open('jokes_json.py')
# citeste
continut = f.readlines()
print(continut)

# inchide fisierul
f.close()


# deschide fisierul pentru scriere
f = open('test.py', "w")
f.write('CEVA....')
f.close()



with open('test.py', "w") as f:
    f.write('ALTCEVA....')
