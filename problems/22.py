# Names scores

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
# first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each
# name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

def alpha_score(string):
    score = 0
    for letter in string:
        value = ord(letter.upper()) - 64
        if 1 <= value <= 26:
            score += ord(letter.upper()) - 64
    return score


assert alpha_score('A') == 1
assert alpha_score('a') == 1
assert alpha_score('z') == 26
assert alpha_score('aa') == 2
assert alpha_score('"aa"') == 2

def main():
    # with open("data/p022_names.txt", "r") as f:
    #     firstline = f.readline().rstrip()
    #
    # print(firstline)
    with open("data/p022_names.txt", "r") as file:
        line = file.read()
        names = line.split(',')
    sorted_names = sorted(names)
    # for i in range(0, 11):
    #     print(sorted_names[i])
    print(sorted_names[937])
    total_score = 0
    for i in range(0, len(sorted_names)):
        total_score += (i+1) * alpha_score(sorted_names[i])
        print("total_score {} += ({} + 1) * alpha_score(sorted_names[i]) {} {}".format(total_score, i, sorted_names[i], alpha_score(sorted_names[i])))
    print("Total score: {}".format(total_score))

main()
