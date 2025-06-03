from sympy import sqrt, isprime

T1 = (sqrt(5) - 1) / 4
J1 = (3 - sqrt(5)) / 4


def golden_prime_generator(limit):
    primes = []
    for n in range(2, limit):
        Fn = ((T1 / J1) ** n - (-J1 / T1) ** n) / sqrt(5)
        val = int(Fn.round())
        if isprime(val):
            primes.append(val)
    return primes


my_primes = golden_prime_generator(1000)
print(my_primes)