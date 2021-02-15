# Maximum path sum II

triangle = []
file = open("data/p067_triangle.txt", "r")
for line in file:
    triangle.append(line.rstrip().split(' '))

# Perform addition of the previous value on each number that is not the very first row, aka top of the triangle.
# Since there are only two possible values to add from the previous row to the current value, use only the
# greater value
for row in range(len(triangle)):
    row_len = len(triangle[row])
    # print(triangle[row])
    for i in range(row_len):
        triangle[row][i] = int(triangle[row][i])
        if row_len > 1:
            tmp_value = 0
            if i > 0 and row > 0:
                tmp_value = triangle[row - 1][i - 1]
            if row > 0 and i + 1 < row_len:
                if triangle[row - 1][i] > tmp_value:
                    tmp_value = triangle[row - 1][i]
            triangle[row][i] += tmp_value

# Get the max value from the last row of the triangle
print(max(triangle[len(triangle) - 1]))