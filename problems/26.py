# Reciprocal cycles
from collections import Counter
import decimal

# This precision value had to be much higher than I originally thought.  Started with just 300 precision
precision_length = 10000
decimal.getcontext().prec = precision_length

longest_original_value = 0
longest_d = 0
longest_d_value = 0
longest_d_len = 0
stopat = 1000
for d in range(2, stopat + 1):
    num = 1 / decimal.Decimal(d)
    num_str = str(num)[2:]  # convert num to a string, removing first 2 characters which are '0.'
    num_length = len(num_str)
    num_count = Counter(num_str)
    num_str_no_repeats = ""
    for i in range(0, num_length):
        if i > 0:
            # print("dbug {} {}".format(num_str[i], num_str[i - 1]))
            if num_str[i] != num_str[i - 1]:
                num_str_no_repeats += num_str[i]
        else:
            num_str_no_repeats += num_str[i]
    # print("num_str_no_repeats {}".format(num_str_no_repeats))
    if len(num_str_no_repeats) > (precision_length *.1):
        # One approach is to take first character and walk the string, stopping at the first repeat of this character
        # then comparing the previous walked substring to the next section
        # the substrings match, we've found our repeating section and we know its length
        # If section doesn't match, continue the walk, if we get to over half way down the string without a match
        # then this character was not a good starter, increment to the next character and repeat process
        # Do this for the first 5 or so characters

        # Walk the first 5 characters after decimal and look for patterns
        for i in range(0, 5 + 1):
            # Quick way to filter same trailing decimal
            # if num_count[num_str[i]] > (precision_length * .8):
            #     break
            starting_character = num_str_no_repeats[i]
            # Only search halfway down the string for a match
            for c in range(i + 1, len(num_str_no_repeats) // 2):
                # print("SC {} current character {}".format(starting_character, num_str_no_repeats[c]))
                if starting_character == num_str_no_repeats[c]:
                    match_substring = num_str_no_repeats[i:c]
                    s_start = i+len(match_substring)
                    s_end = s_start + len(match_substring)
                    n_start = s_end + len(match_substring)
                    n_end = n_start + len(match_substring)
                    # print("d {} ms {} next substring {} next sub {}".format(d, match_substring, num_str_no_repeats[s_start:s_end], num_str_no_repeats[n_start:n_end]))
                    if (match_substring == num_str_no_repeats[s_start:s_end] == num_str_no_repeats[n_start:n_end]):
                        # print("MATCH FOUND!")
                        match_found = True
                        if len(match_substring) > longest_d_len:
                            longest_d = d
                            longest_original_value = num
                            longest_d_len = len(match_substring)
                            longest_d_value = match_substring
                            print("{} takes the lead! {} {}".format(longest_d, longest_d_len, longest_d_value))
                        # print("match found! {}".format(num_str_no_repeats[i:c]))
                        break
            if match_found:
                break

print("longest d {}, Longest repeating length {} longest_d_value {} original value: {}".format(longest_d, longest_d_len, longest_d_value, longest_original_value))