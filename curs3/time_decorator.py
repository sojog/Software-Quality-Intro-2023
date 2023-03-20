import time


print(time.time())


def timer(func):
    def replace_func(n):
        t1 = time.time()
        rezultat = func(n)
        t2 = time.time()
        print(f'functia a fost executa in {(t2 - t1)} secunde')
        return rezultat

    return replace_func


@timer
def suma(n):
    return sum(range(n))


print(suma(100))


@timer
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1)*n

# t1 = time.time()
# # time.sleep(1)
# print(factorial(100))
# t2 = time.time()

# print(f'functia a fost executa in {(t2 - t1)} secunde')


@timer
def fibonacci(n):
    if n == 1 or n ==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# t1 = time.time()
# print(fibonacci(30))
# t2 = time.time()
# print(f'functia a fost executa in {(t2 - t1)} secunde')


# print(fibonacci(6))
# print(factorial(1))
