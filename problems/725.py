# Digit sum numbers

# where 1 digit is the sum of all the OTHER digits is called a digit sum number or DSN for short
# i.e. 352  3 + 2 = 5, 3003  3 + 0 + 0 = 3,  32812  3 + 2 + 1 + 2 = 8

# S(n) is the sum of all DSN of n digits or less
# given S(3) = 63270 and S(7) = 85499991450
# find S(2020)  Give answer modulo 10**16   aka  sum % 10**16 = answer
from math import floor


def combinations_of_dsn(max_length_of_digits):
    # 1 digit length is incompatible so start n must be greater than 2
    # the 0 digit will allow a lot of combinations

    # len(n) == 2 has possibilities, because only mirror values, 11, 22, 33
    total_dsn = 9

    # n_len = len(str(n))
    other_digit_locations = max_length_of_digits - 1
    full_combinations = max_length_of_digits * other_digit_locations
    half_combinations = full_combinations // 2
    all_zero_combinations = 9 * other_digit_locations
    total_dsn += all_zero_combinations
    print("max digits {} full_combinations {} half_combinations {} all_zero_combinstions {} ".format(max_length_of_digits, full_combinations, half_combinations, all_zero_combinations))
    for dsn in range(1, 9 + 1):
        if dsn == 1:
            total_dsn += other_digit_locations
        else:
            if dsn % 2 == 0:
                total_dsn += ((dsn / 2) - 1) * full_combinations
                total_dsn += half_combinations
            else:
                total_dsn += floor(dsn / 2) * full_combinations

    return total_dsn

print(combinations_of_dsn(3))
# assert sum_of_dsn(3) == 63270


# # combinations for 1 will just be the len - 1 positions
#
# 101
# 110
#
# # if dsn is even, this eliminates at least 1 position swap of OTHER numbers
# # let O be len(n) - 1 and mean number of OTHER positions
# # O**dsn positions - funky stuff
# # 3 positions, 3 digits 0, 1, 2
# # 2 + 0 = 2
# # 1 + 1 = 2
# # a 0 means the left most position is unavailable for however many 0's are considered.
# 202
# 220
#
# 211
# 112
# 121
#
# 303
# 330
#
# 312
# 213
# 321
# 123
# 132
# 231
#
# # for identical OTHER digit, the 0's situation, there are len(n) - 1 DSN
# 404
# 440
#
# 413
# 314
# 431
# 134
# 143
# 341
#
# 422
# 224
# 242

# 8 = dsn, length = 3, workable length = 2
# 808
# 880
#
# 817
# 871
# 187
# 781
# 178
# 718
#
# 826
# 862
# 286
# 682
# 268
# 628
#
# 835
# 853
# 385
# 583
# 358
# 538
#
# 844
# 484
# 448
#
# # 23 combos for dsn of 8 and n len of 3
# # can't do anything beyond the breakeven point for 2 locations
#
# 909
# 990
#
# 918
# 981
# 198
# 891
# 189
# 819
#
# 927
#
# 936
#
# 945
#
# # 26 combos for dsn of 9 and n len of 3

