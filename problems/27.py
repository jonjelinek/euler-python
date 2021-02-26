# Quadratic primes

# Find the product of the coefficents a and b  for following quadratic expression that produces the maximum number of
# consecutive primes

# n**2 + (a * n) + b   where |a| < 1000 and |b| <= 1000

# Approach is to calculate value of each iteration of expression combination till n = 100?
# then create a set of primes up to a certain number, maybe the max number computed
# then go through the array and quickly check each value against prime set
# recording the longest consecutive


# optimization, determine largest value, max a and max b
# then build out the primes table till that number
# then loop through and record longest consecutive primes

from shared.functions import find_primes

n_size = 10**2
a_size = 999
b_size = 1000

largest_computed = n_size**2 + (a_size * n_size) + b_size
primes = find_primes(largest_computed + 1)

print("primes calculated.  prime list size {}".format(len(primes)))

longest_prime_a_b = (0, 0)
longest_n = 0
for a in range((-1 * a_size), a_size + 1):
    print(a, end=',')
    for b in range((-1 * b_size), b_size + 1):
        n = 0
        quad = abs((n**2 + (a * n) + b))
        while quad in primes:
            n += 1
            quad = abs((n ** 2 + (a * n) + b))
            if quad > largest_computed:
                print("{} is beyond largest known prime. Expanding primes list. current size {}".format({}, len(primes)))
                primes = find_primes(quad * 2, primes)
                print("New primes list size {}".format(len(primes)))

        if n > longest_n:
            longest_prime_a_b = (a, b)
            longest_n = n
            print("{} has consecutive prime length of {}".format(longest_prime_a_b, longest_n))


print("{}".format(longest_prime_a_b[0] * longest_prime_a_b[1]))