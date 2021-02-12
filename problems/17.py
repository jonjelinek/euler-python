# Number letter counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance
# with British usage.


# 0 = zero = 4, 1 = one = 3 letters, 2 = two = 3 letters
# zero through 9
digit = [4, 3, 3, 5, 4, 4, 3, 5, 5, 4]

words = {
    'hundred': 7,
    'and': 3,
    'thousand': 8,
}

lookup = {
    10: len('ten'),
    11: len('eleven'),
    12: len('twelve'),
    13: len('thirteen'),
    14: len('fourteen'),
    15: len('fifteen'),
    16: len('sixteen'),
    17: len('seventeen'),
    18: len('eighteen'),
    19: len('nineteen'),
    20: len('twenty'),
    30: len('thirty'),
    40: len('forty'),
    50: len('fifty'),
    60: len('sixty'),
    70: len('seventy'),
    80: len('eighty'),
    90: len('ninety'),
}

def get_letter_count(start, finish):
    total_letters = 0
    for i in range(start, finish + 1):
        num = [int(i) for i in str(i)]
        # print(num)
        if len(num) == 3:
            total_letters += digit[num[0]] + words['hundred']
            if i % 100 != 0:
                total_letters += words['and']
                i = int(str(num[1]) + str(num[2]))
                num = [int(i) for i in str(i)]
        if len(num) == 1:
            total_letters += digit[i]
        else:
            if len(num) == 2:
                if i < 20:
                    total_letters += lookup[i]
                else:
                    if i % 10 == 0:
                        total_letters += lookup[i]
                    else:
                        # print("i = {}, i // 10 = {}, lookup[i // 10] = {}".format(i, i // 10, lookup[i // 10 * 10]))
                        total_letters += lookup[i // 10 * 10] + digit[num[1]]
        if i % 1000 == 0:
            total_letters += digit[1] + words['thousand']

    return total_letters


assert get_letter_count(1, 5) == 19

print(get_letter_count(1, 1000))

# previous wrong answers:
# 21234 - calculated length of 40 incorrectly because of a misspelling
# 21134 - was adding 'eight' + 'teen' when the actual word is 'eighteen'