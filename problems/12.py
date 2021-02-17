# highly divisible triangular number
# triangular number is found by adding natural numbers, i.e. 7th tri num is 1+2+3+4+5+6+7 = 28
# 28 is the first triangular number to have 5 divisors: 1,2,4,7,14,28
# Find the first triangular number to have over 500 divisors
from shared.functions import get_num_of_divisors

step = 1
triangular_number = 1
while get_num_of_divisors(triangular_number) < 500:
    if step % 100 == 0:
        print("progress: tri num {} on step {} number of divisors {}".format(triangular_number, step, get_num_of_divisors(triangular_number) ))
    step += 1
    triangular_number += step


print("final tri num {} on step {}".format(triangular_number, step))
