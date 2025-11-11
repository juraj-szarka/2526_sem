import time

def get_prime(number):
    divider = 2
    if number == 1:
        return False
    while divider <= (number ** 0.5):
        if number % divider == 0:
            return False
        else:
            divider += 1
    return True

def get_primes(mini: int, maxi: int) -> None:
    for i in range(maxi - mini + 1):
        if get_prime(i + mini):
            print(i + mini)
    return None

def start():
    mini = int(input('Zadaj minimum: '))
    maxi = int(input('Zadaj maximum: '))
    get_primes(mini, maxi)
    return None

start()
