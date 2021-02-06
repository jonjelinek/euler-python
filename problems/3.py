# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

known_primes = [2, 3, 5, 7, 11, 13, 17, 19]
prime_factors = []

def find_primes(number: int):
    # loop from 2 up, until find something divisible.
    # if num is 2, 3, 5, 7
    if number in known_primes:
        prime_factors.append(number)
        return
    else:
        for prime in known_primes:
            if number % prime == 0:
                prime_factors.append(prime)
                find_primes(number // prime)
                return
        for divisor in range(4, (number // 2)):
            if number % divisor == 0:
                prime_factors.append(divisor)
                find_primes(number // divisor)
                return
        prime_factors.append(number)
        # raise Exception(prime_factors, number)
        return

find_primes(600851475143)
print(prime_factors)
