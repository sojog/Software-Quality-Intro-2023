
a = 2
b = 3

# Varianta 1
aux = a
a = b
b = aux
print("a=", a)
print("b=", b)

# Varianta 2 - packing si unpacking
a, b = (b, a)
print("a=", a)
print("b=", b)

