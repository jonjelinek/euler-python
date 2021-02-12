# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner
# How many such routes are there through a 20×20 grid?

def number_of_routes(position, end):
    result = 0
    # print(position)
    if position == end:
        # print("end")
        return 1
    if position[0] != end[0]:
        result += number_of_routes((position[0] + 1, position[1]), end)
    if position[1] != end[1]:
        result += number_of_routes((position[0], position[1] + 1), end)
    return result

assert number_of_routes((0, 0), (2, 2)) == 6

print(number_of_routes((0, 0), (20, 20)))
