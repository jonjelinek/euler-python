# Lattice paths

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


# Second attempt, going to focus on making as simple of a recursive function as possible
def right_down_route(right, down, end):
    if right > end:
        return 0
    if down > end:
        return 0
    if right + down == end * 2:
        return 1
    return right_down_route(right + 1, down, end) + right_down_route(right, down + 1, end)


# for end in range(2, 21):
#     print("end: {} routes: {}".format(end, right_down_route(0, 0, end)))


# Previous methods too slow!!  Going to try and just create a grid and do the calculations.

import copy

rows, cols = (20 + 1, 20 + 1)
# Create the grid
arr = [[0 for c in range(cols)] for r in range(rows)]
# Fill top row with 1's
arr[0][0] = 1

# Going left to right, if a spot == 0, set its values to previous_row + previous_col
for row in range(rows):
    for col in range(cols):
        previous_row = 0 if row == 0 else row - 1
        previous_col = 0 if col == 0 else col - 1
        if arr[row][col] == 0:
            arr[row][col] = arr[row][previous_col] + arr[previous_row][col]

# Prints the grid for visual effect
for row in arr:
    print(row)

# Print just the answer
print(arr[20][20])
