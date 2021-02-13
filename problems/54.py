# Given file data/p054_poker.txt which contains 1000 hands of poker
# the first 5 cards are for player 1 then a space and then the second 5 cards
# How many hands does player 1 win?
# More details at: https://projecteuler.net/problem=54

from collections import Counter


def get_card_value(v):
    if v == 'T':
        return 10
    if v == 'J':
        return 11
    if v == 'Q':
        return 12
    if v == 'K':
        return 13
    if v == 'A':
        return 14
    return int(v)


def straight(v):
    sorted_values = sorted(v)
    consecutive_list = list(range(min(v), max(v) + 1))
    if sorted_values == consecutive_list:
        return True
    return False


def flush(counts):
    for key in counts:
        if counts[key] == 5:
            return True
    return False


def straight_flush(v,suits):
    if straight(v) and flush(Counter(suits)):
        return True
    return False


def royal_flush(v, suits):
    if straight_flush(v, suits):
        if max(v) == 14:
            return True
    return False


def four_kind(counts):
    for key in counts:
        if counts[key] >= 4:
            return True
    return False


def three_kind(counts):
    for key in counts:
        if counts[key] >= 3:
            return True
    return False


def pair(counts):
    for key in counts:
        if counts[key] >= 2:
            return True
    return False


def two_pair(counts):
    pairs = 0
    for key in counts:
        if counts[key] >= 4:
            pairs += 2
        else:
            if counts[key] >= 2:
                pairs += 1
    if pairs >= 2:
        return True
    return False


def full_house(counts):
    if three_kind(counts):
        for key in counts:
            if counts[key] == 2:
                return True
    return False


def high_card(v):
    return max(v)


def get_values_and_suits(line):
    values = [line[0][:1], line[1][:1], line[2][:1], line[3][:1], line[4][:1]]
    values = [get_card_value(v) for v in values]
    # if 14 in values:
    #     values.append(1)    # Add a 1 to the values to represent the Aces 1 value.
    suits = [line[0][1:2], line[1][1:2], line[2][1:2], line[3][1:2], line[4][1:2]]
    return values, suits


def get_poker_score(values, suits):
    values_counts = Counter(values)
    highest_card_value = 14

    rf = 9 + highest_card_value
    sf = 8 + highest_card_value
    fk = 7 + highest_card_value
    fh = 6 + highest_card_value
    fl = 5 + highest_card_value
    st = 4 + highest_card_value
    tk = 3 + highest_card_value
    tp = 2 + highest_card_value
    op = 1 + highest_card_value

    if royal_flush(values, suits):
        return rf
    if straight_flush(values, suits):
        return sf
    if four_kind(values_counts):
        return fk
    if full_house(values_counts):
        return fh
    if flush(values_counts):
        return fl
    if straight(values):
        return st
    if three_kind(values_counts):
        return tk
    if two_pair(values_counts):
        return tp
    if pair(values_counts):
        return op

    return 0    # high_card(values)


def main():
    file = open("data/p054_poker.txt", "r")
    p1_wins = 0
    p2_wins = 0
    for line in file:
        line = line.split(' ')
        p1_cards = [line[0], line[1], line[2], line[3], line[4]]
        p2_cards = [line[5], line[6], line[7], line[8], line[9]]
        p1_values, p1_suits = get_values_and_suits(p1_cards)
        p2_values, p2_suits = get_values_and_suits(p2_cards)
        p1_score = get_poker_score(p1_values, p1_suits)
        p2_score = get_poker_score(p2_values, p2_suits)
        if p1_score > p2_score:
            p1_wins += 1
        else:
            if p2_score > p1_score:
                p2_wins += 1
            else:
                # Identical score, hand with highest sum wins
                if sum(p1_values) > sum(p2_values):
                    p1_wins += 1
                else:
                    p2_wins += 1
    print("Player 1 won {} games, and Player 2 won {} games.".format(p1_wins, p2_wins))


assert get_card_value('T') == 10
assert get_card_value('J') == 11
assert get_card_value('Q') == 12
assert get_card_value('K') == 13
assert get_card_value('A') == 14

assert four_kind(Counter([10, 10, 10, 13, 10])) is True
assert four_kind(Counter([5, 12, 3, 13, 10])) is False

assert three_kind(Counter([10, 10, 10, 13, 10])) is True
assert three_kind(Counter([5, 12, 3, 13, 10])) is False

assert pair(Counter([10, 10, 10, 13, 10])) is True
assert pair(Counter([5, 12, 3, 13, 10])) is False

assert two_pair(Counter([10, 10, 10, 13, 10])) is True
assert two_pair(Counter([5, 12, 3, 13, 10])) is False

assert full_house(Counter([10, 5, 10, 5, 10])) is True
assert full_house(Counter([2, 5, 10, 5, 10])) is False
assert full_house(Counter([5, 5, 5, 5, 10])) is False

assert flush(Counter(['D', 'D', 'D', 'D', 'D'])) is True
assert flush(Counter(['D', 'D', 'H', 'D', 'D'])) is False

assert straight([2, 3, 4, 5, 6]) is True
assert straight([8, 9, 10, 11, 12]) is True
assert straight([4, 9, 10, 11, 12]) is False

assert straight_flush([2, 3, 4, 5, 6], ['D', 'D', 'D', 'D', 'D']) is True
assert straight_flush([8, 9, 10, 11, 12], ['C', 'C', 'C', 'C', 'C']) is True
assert straight_flush([8, 9, 10, 11, 12], ['C', 'H', 'C', 'D', 'C']) is False
assert straight_flush([10, 11, 12, 13, 14], ['D', 'D', 'D', 'D', 'D']) is True

assert royal_flush([10, 11, 12, 13, 14], ['D', 'D', 'D', 'D', 'D']) is True
assert royal_flush([10, 11, 12, 13, 14], ['D', 'C', 'D', 'D', 'D']) is False

assert high_card([10, 11, 12, 13, 14]) == 14
assert high_card([2, 2, 2, 4, 2]) == 4

main()

# wrong answers: 375