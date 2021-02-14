from math import sqrt

# known_primes is used here to feed the list of primes back into the function to continue finding new primes
# from the last known prime number.  Providing invalid list will result in inaccurate result
def find_primes(stop_at: int, known_primes=None):
    if known_primes is None:
        known_primes = [2]
    current_number = known_primes[-1] + 1
    while current_number < stop_at:
        prime_not_found = True
        for prime in known_primes:
            # Going to the half value was unnecessary.  To understand why sqrt(current_number) is the stopping point
            # look at https://labuladong.gitbook.io/algo-en/iv.-high-frequency-interview-problem/print_primenumbers
            if prime > sqrt(current_number):
                break
            if current_number % prime == 0:
                prime_not_found = False
                break
        if prime_not_found:
            # print("{}".format(current_number), end=' ')
            known_primes.append(current_number)
        current_number += 1
    return known_primes