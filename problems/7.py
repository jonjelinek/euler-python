# finding the nth prime number

# given the first 6 prime numbers: 2,3,5,7,11,13  what is the 10,001 prime number
known_primes = [2, 3, 5, 7, 11, 13]

def nth_prime_number(n):
    if len(known_primes) >= n:
        return known_primes[n-1]
    current_number = known_primes[-1] + 1
    while len(known_primes) < n:
        half_val = current_number / 2
        prime_not_found = True
        for prime in known_primes:
            if prime > half_val:
                break
            if current_number % prime == 0:
                prime_not_found = False
                break
        if prime_not_found:
            known_primes.append(current_number)
        current_number += 1
    print(known_primes)
    return known_primes[-1]



assert nth_prime_number(6) == 13

print(nth_prime_number(10001))