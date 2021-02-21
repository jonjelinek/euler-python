# Non-abundant sums

# an abundant number is a number whose proper divisors add up to more than the number itself
# The problem states that mathematical analysis shows after 28123 all numbers can be written as
# sum of two abundant numbers
# find the sum of all positive integers which cannot be written as the sum of two abundant numbers

from shared.functions import get_proper_divisors

assert sum(get_proper_divisors(12)) == 16

the_list = [1] * (28123 + 1)
abundant_numbers = set()
sum_of_positive_integers_not_sum_of_two_abundant_divisors = 0
limit = 28123
#limit = 24
for n in range(1, limit + 1):
    proper_divs = get_proper_divisors(n)
    # print("n {} proper divs {}".format(n, proper_divs))
    if len(proper_divs) > 1:
        # See if 2 or more divisors intersect the proper_divs and abundant_numbers sets
        if len(proper_divs & abundant_numbers) >= 1:
            # Then this number is made up of 2 or more abundant numbers... possibly not exactly what we want
            # If intersecting divisor is n / 2, then this disqualifies it
            # Otherwise must compare the combinations of all? intersecting divisors?
            #   Probably optimization here to go from largest to smallest, and if divisor being checked is under n / 2
            #   then the number should be passed
            # print("max divs {}".format(max(proper_divs)))
            if not max(proper_divs) * 2 == n:
                # print("29 adding {} to sum".format(n))
                sum_of_positive_integers_not_sum_of_two_abundant_divisors += n
                # for div in proper_divs:
                #     if len({n - div} & abundant_numbers) == 1:
                #         # We have 2 abundant divisors so we need to not include this number
                #         break
        else:
            # print("35 adding {} to sum".format(n))
            sum_of_positive_integers_not_sum_of_two_abundant_divisors += n
        if sum(proper_divs) > n:
            # print("adding {} to abundant numbers".format(n))
            abundant_numbers.add(n)
    else:
        # print("42 adding {} to sum".format(n))
        sum_of_positive_integers_not_sum_of_two_abundant_divisors += n

print(abundant_numbers)

for ab in sorted(abundant_numbers,reverse=True):
    targets = set(filter(lambda x: x <= (limit - ab), abundant_numbers))
    # print("For ab {} length of targets are {}".format(ab, len(targets)))
    for t in targets:
        if t + ab < limit + 1:
            the_list[t + ab] = 0
    abundant_numbers.remove(ab)

print(sum_of_positive_integers_not_sum_of_two_abundant_divisors)

print(the_list)
# print(sum(set(filter(lambda x: x == 1, the_list))))
total = 0
for n in range(1, limit + 1):
    if the_list[n] == 1:
        total += n

print(total)
# wrong 40872647
# wrong 317090642
# wrong 310289560