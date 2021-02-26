from math import sqrt
import time


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


def get_num_of_divisors(num):
    divisor_count = 2
    for x in range(2, int(sqrt(num))):
        if num % x == 0:
            divisor_count += 2
    return divisor_count


def get_proper_divisors(num):
    divisors = set()
    for x in range(2, int(sqrt(num)) + 1):
        if num % x == 0:
            divisors.add(x)
            divisors.add(int(num / x))

    divisors.add(1)
    return divisors


def get_divisors(num):
    divisors = get_proper_divisors(num)
    divisors.add(num)
    return divisors


# This needs work, it doesn't seem to time the function exactly
# For example, if arguments are determined ahead of time, they're excluded from the timing
def time_function(f):
    start = time.time()
    f
    end = time.time()
    print("Took %f ms" % ((end - start) * 1000.0))


def fib(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    previous_fi = 0
    fi = 1
    for n in range(i - 1):
        temp = fi
        fi = fi + previous_fi
        previous_fi = temp
    return fi