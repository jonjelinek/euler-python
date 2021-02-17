# Consecutive positive divisors

# Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same number of positive divisors.
# For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

from shared.functions import get_num_of_divisors, find_primes, get_divisors


def brute_force_method(stop_num):

    previous = 0
    current = 0
    total_n_same_as_next_divisors = 0

    for n in range(1, stop_num + 2):
        if n % 1000 == 0:
            print("finding divisors {}".format(n))
        current = get_num_of_divisors(n)
        if previous == current:
            total_n_same_as_next_divisors += 1
        previous = current
        # total_divisors[n] = get_num_of_divisors(n)

    # previous_num_divisors = 0
    # for n in range(1, stop_num + 1):
    #     if total_divisors[n] == total_divisors[n + 1]:
    #         total_n_same_as_next_divisors += 1

# optimized version would be to fill out an array
# key off the primes, determine prime*2 divisors, and then for each number that is prime*2**n will be the set of those divisors * 2 * n

def clever_method_building_out_lists_of_the_divs(end_num):
    # total_divisors_num_list = list(range(0, end_num + 2))
    total_divisors_num_list = [None] * (end_num + 1)
    primes = find_primes(end_num)
    total_consecutive_matches = 0

    for prime in primes:
        divs = set()
        one = 1
        while prime <= end_num:
            divs.add(one)
            divs.add(prime)
            total_divisors_num_list[prime] = divs
            one *= 2
            prime *= 2
            divs = divs.copy()

    for i in range(0, len(total_divisors_num_list)):
        if i % 1000 == 0:
            print(i)
        if total_divisors_num_list[i] is None:
            total_divisors_num_list[i] = get_divisors(i)

    for i in range(0, len(total_divisors_num_list)):
        if total_divisors_num_list[i] == total_divisors_num_list[i + 1]:
            total_consecutive_matches += 1

    return total_consecutive_matches


def clever_method(end_num):
    print("building list")
    num_list = set(range(1, end_num + 1))
    total_divisors_num_list = [None] * (end_num + 1)
    print("finding primes")
    primes = find_primes(end_num)
    total_consecutive_matches = 0

    print(len(num_list))
    print("setting prime divisors count")

    prime = 2
    num_divs = 2
    while prime <= end_num:
        total_divisors_num_list[prime] = num_divs
        prime *= 2
        num_divs += 1
    primes.remove(2)
    for prime in primes:
        num_divs = 2
        while prime <= end_num:
            total_divisors_num_list[prime] = num_divs
            num_list.remove(prime)
            prime *= 2
            num_divs += 2

    print("setting non prime divisors count")
    # for i in range(0, len(total_divisors_num_list)):
    #     if i % 1000 == 0:
    #         print(i)
    #     if total_divisors_num_list[i] is None:
    #         total_divisors_num_list[i] = len(get_divisors(i))

    for num in num_list:
        # print(num)
        total_divisors_num_list[num] = len(get_divisors(num))


    for i in range(2, len(total_divisors_num_list) - 1):
        if total_divisors_num_list[i] == total_divisors_num_list[i + 1]:
            total_consecutive_matches += 1

    with open('problem_179_output.txt', 'w') as file_object:
        file_object.write(str(total_divisors_num_list))

    return total_consecutive_matches


# print(brute_force_method(10**7))
print(clever_method(10**7))

# incorrect answers: brute force method 986234