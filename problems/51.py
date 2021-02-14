# prime digit replacements

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible
# values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example
# having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773,
# and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same
# digit, is part of an eight prime value family.

# For any prime number, replace up to n values with an identical digit. For that digit being 0 to 9, find the smallest
# prime number where this replacement of n digits produces an 8 prime family.

from shared.functions import find_primes

assert find_primes(10) == [2, 3, 5, 7]

# the 2 digit number given.  D - being the digit(s), a or b being the first or second number
# need to check the lowest numbers first, so in a two digit that would be doing aD incrementation
# i.e. a = 1: 10, 11, 12, 13, 14, 15, 16

# in a 3 digit number, where D is 1 digit, this would look like
# abD, a = 1, b = 0, 100, 101, 102, 103...
# but when we get to DD is there may be an optimization?
# aDD, 100, 111, 122, 133...
# finally the full replacement
# DDD, 111, 222, 333, 444
# perhaps it's best to work backwards from the full replacement on down.
# DDD could only be beaten if there was an aDD solution and aDD beaten if there were an abD solution

# set method
# d = []
# for i in list(range(0, len(str(sorted_two_digital_primes[0])))):
#     d.append(set({}))
# for num in sorted_two_digital_primes:
#     for i in range(0, len(str(num))):
#         # print("d[{}].add(str({})[len({}) - {}])".format(i, num, len(str(num)) - 1, i))
#         d[i].add(int(str(num)[(len(str(num)) - 1) - i]))
# print(d)


def get_lowest_prime_from_prime_family_of_size(size, primes_list):
    # array method, have multi demensional array of lengths [0-9] = 0 for all digits, then increment the times that digit was seen while stepping through all of the known primes numbers
    target_prime_family_group_number = size

    # shouldn't actually need to be a sorted list
    # len_of_nums = len(str(sorted_two_digital_primes[0]))
    len_of_nums = len(str(primes_list[0]))

    d = []
    for i in range(len_of_nums):
        # Each 0 represents the count of how many times that number appears, i.e. d[0][3] would store the value for the number of times 3 appeared in 0 digit location
        d.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    for num in primes_list:
        for i in range(0, len(str(num))):
            # print("d[{}].add(str({})[len({}) - {}])".format(i, num, len(str(num)) - 1, i))
            # d[i].add(int(str(num)[(len(str(num)) - 1) - i]))
            # print("d[{}][int(str({})[i:i+1])]  d[{}][{}]".format(i, num, i, int(str(num)[i:i+1])))
            d[i][int(str(num)[i:i+1])] += 1
    # print(d)

    # loops backwards, so it checks the lowest digit first
    list_of_family = []
    for i in range(len_of_nums -1, -1, -1):
        # for n in d[i]:
        #     print("d[i] i {} {}".format(i, d[i]))
        #     print("d[{}][{}] val {}".format(i, n, d[i][n]))
        #     if d[i][n] >= target_prime_family_group_number:
        #         print("Found something!")
        #         for num in primes_list:
        #             if int(str(num)[i:i+1]) == d[i].index(n):
        #                 list_of_family.append(num)

        if target_prime_family_group_number in d[i]:
            # print("target {} found: i {} value {}".format(target_prime_family_group_number, i, d[i].index(target_prime_family_group_number)))
            for num in primes_list:
                if int(str(num)[i:i+1]) == d[i].index(target_prime_family_group_number):
                    list_of_family.append(num)

    if list_of_family:
        print("Lowest prime {} in a prime family size of {}".format(min(list_of_family), target_prime_family_group_number))
        return min(list_of_family)

    return None


def main():
    single_digit_prime_list = find_primes(9)
    print(single_digit_prime_list)
    # [:] ensures we're only passing a copy of single_digit_prime_list, as the list address is what is passed normally
    # which causes side effects since the function ends up modifying the list
    two_digit_number_prime_list = find_primes(99, single_digit_prime_list[:])
    print(single_digit_prime_list)
    print(two_digit_number_prime_list)
    # print(sorted(list(set(two_digit_number_prime_list) - set(single_digit_prime_list))))
    # print(list(set(two_digit_number_prime_list) - set(single_digit_prime_list)))

    unsorted_two_digital_primes = list(set(two_digit_number_prime_list) - set(single_digit_prime_list))
    sorted_two_digital_primes = sorted(list(set(two_digit_number_prime_list) - set(single_digit_prime_list)))

    print(get_lowest_prime_from_prime_family_of_size(6, sorted_two_digital_primes))
    assert get_lowest_prime_from_prime_family_of_size(6, sorted_two_digital_primes) == 13
    assert get_lowest_prime_from_prime_family_of_size(6, unsorted_two_digital_primes) == 13

    # print(get_lowest_prime_from_prime_family_of_size(7, sorted_two_digital_primes))

    print("-------------------------")
    target_family_size = 6
    max_number = 9
    primes = find_primes(max_number)
    current_primes = primes[:]
    lowest_target_prime = None
    while lowest_target_prime is None:
        lowest_target_prime = get_lowest_prime_from_prime_family_of_size(target_family_size, current_primes)
        if lowest_target_prime is None:
            max_number = int(str(max_number) + "9")
            new_primes = find_primes(max_number, primes[:])
            current_primes = list(set(new_primes) - set(primes))
            primes = new_primes
            print("new max number {}\nnew primes: {}".format(max_number, current_primes))

    print("Found lowest prime {} for min prime family size of {}".format(lowest_target_prime, target_family_size))


main()
