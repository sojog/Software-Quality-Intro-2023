def fun(x = 4, y = 5):
    print("x=", x, "y=", y)
    y -= 1
    return x * y * 1
print(fun())