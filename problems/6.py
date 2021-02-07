# sum square difference

def sum_square_diff(first, last):
    sum_of_squares = 0
    sum_of_numbers = 0
    for i in range(first, last + 1):
        sum_of_squares += i * i
        sum_of_numbers += i
    answer = sum_of_numbers * sum_of_numbers - sum_of_squares
    # print(answer)
    return answer

assert sum_square_diff(1, 10) == 2640

print(sum_square_diff(1,100))