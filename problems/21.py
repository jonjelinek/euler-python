# Amicable numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

from math import sqrt


def get_divisors(num):
    divisors = set()
    for x in range(2, int(sqrt(num))):
        if num % x == 0:
            divisors.add(x)
            divisors.add(int(num / x))

    divisors.add(1)
    return divisors


def sum_divisors(num):
    return sum(get_divisors(num))


assert sum_divisors(0) == 1
assert sum_divisors(1) == 1
assert sum_divisors(2) == 1
assert sum_divisors(3) == 1
# print(get_divisors(220))
assert sum_divisors(220) == 284

d_sum = []
for number in range(0, 10000 + 1):
    d_sum.append(sum_divisors(number))

amicable_numbers = set()
for number in range(0, 10000 + 1):
    if d_sum[number] != number:
        if d_sum[number] < 10000:
            if d_sum[d_sum[number]] == number:
                print("Amicable numbers found {} {}".format(number, d_sum[number]))
                amicable_numbers.add(number)
                amicable_numbers.add(d_sum[number])

print(sum(amicable_numbers))

# wrong answer 63252
