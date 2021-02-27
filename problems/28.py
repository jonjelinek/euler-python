# Number spiral diagonals

size = 1001
spiral = [[0 for c in range(size)] for r in range(size)]

pos = (size // 2, size // 2)

move_right = lambda x, y: (x, y + 1)
move_down = lambda x, y: (x + 1,y)
move_left = lambda x, y: (x, y - 1)
move_up = lambda x, y: (x - 1, y)

n = 1
diag_sum = n
spiral[pos[0]][pos[1]] = n
for steps in range(2, 2*(size // 2) + 1, 2):
    pos = move_right(pos[0], pos[1])
    n += 1
    spiral[pos[0]][pos[1]] = n
    for s in range(steps - 1):
        n += 1
        pos = move_down(pos[0], pos[1])
        spiral[pos[0]][pos[1]] = n
    diag_sum += n
    for s in range(steps):
        n += 1
        pos = move_left(pos[0], pos[1])
        spiral[pos[0]][pos[1]] = n
    diag_sum += n
    for s in range(steps):
        n += 1
        pos = move_up(pos[0], pos[1])
        spiral[pos[0]][pos[1]] = n
    diag_sum += n
    for s in range(steps):
        n += 1
        pos = move_right(pos[0], pos[1])
        spiral[pos[0]][pos[1]] = n
    diag_sum += n

print(diag_sum)