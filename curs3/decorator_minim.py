


def minim_zero(func):
    def wrapper_function(n):
        if n < 0:
            return 0 
        else:
            return func(n)
    return wrapper_function



@minim_zero
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1)*n


@minim_zero
def fibonacci(n):
    if n == 1 or n ==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(-10))