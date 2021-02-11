# Longest Collatz sequence

# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?

even = lambda n : n / 2
odd = lambda n : 3 * n + 1

def collatz_length(number):
    length = 1
    while number != 1:
        if number % 2 == 0:
            number = even(number)
        else:
            number = odd(number)
        length += 1
    return length

assert collatz_length(13) == 10

longest_collatz_chain = 0
longest_number = 0
for x in range(1, 1000000 + 1):
    test_length = collatz_length(x)
    if test_length > longest_collatz_chain:
        print("New longest chain found: number {}, length {}".format(x, test_length))
        longest_collatz_chain = test_length
        longest_number = x

print("finished")