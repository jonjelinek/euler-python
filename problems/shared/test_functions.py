from functions import find_primes, get_num_of_divisors, time_function

assert find_primes(10) == [2, 3, 5, 7]
assert find_primes(10, [2, 3, 5]) == [2, 3, 5, 7]
# assert find_primes(10)
assert get_num_of_divisors(14) == 4
assert get_num_of_divisors(28) == 6

# Not too useful, this timing functionality needs work
# time_function(find_primes(10**6))