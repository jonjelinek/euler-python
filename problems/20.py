# Factorial digit sum

# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

def fac(n):
    product = 1
    for m in range(1, n + 1):
        product *= m
    return product


def digit_sum(num):
    return sum([int(i) for i in str(num)])


assert fac(10) == 3628800
assert digit_sum(fac(10)) == 27
print(digit_sum(fac(100)))
