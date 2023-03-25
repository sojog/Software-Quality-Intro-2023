raspuns = [{'score': 4067, 'word': 'clear'},
 {'score': 1804, 'word': 'bright'},
 {'score': 1675, 'word': 'gay'},
 {'score': 981, 'word': 'cheerful'},
 {'score': 881, 'word': 'shiny'},
 {'score': 534, 'word': 'shining'},
 {'score': 411, 'word': 'cheery'},
 {'score': 265, 'word': 'sunshiny'}]

# Varianta 1 - iterare clasica
cuvinte = []
for i in raspuns:
    print(i, type(i))
    print(i['word'])
    cuvinte.append(i['word'])

print(cuvinte)

# Varianta 2 - list comprehention
cuvinte = [  i['word']    for i in raspuns  ]
print(cuvinte)