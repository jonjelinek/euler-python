# Lattice points on a circle

# Watched this video on a refresher for determining if a coordinate is on the line
# https://www.khanacademy.org/math/geometry/hs-geo-analytic-geometry/hs-geo-dist-problems/v/point-relative-to-circle#:~:text=First%2C%20find%20the%20equation%20for,is%20inside%20of%20the%20circle.
from math import sqrt
import time


def find_distance_from_center_of_circle(circle_center, coordinate):
    return sqrt((circle_center[0] - coordinate[0])**2 + (circle_center[1] - coordinate[1])**2)


# Let f(N) be the number of points with integer coordinates that are on a circle passing through (0,0), (N,0),(0,N), and (N,N).
def original_f(N):
    y = N
    x = 1
    integer_coordinates = 0
    quadrants = 4
    circle_center = (0, 0)
    while x <= N:
        # dis = find_distance_from_center_of_circle(center, (x, y))
        dis = sqrt((circle_center[0] - x) ** 2 + (circle_center[1] - y) ** 2)
        # print("debug: {} {}".format((x, y), dis))
        if dis > N:
            # print("down")
            y -= 1
        else:
            if dis < N:
                # print("right")
                x += 1
            else:
                integer_coordinates += 1
                print("{}".format((x, y)))
                x += 1
    return integer_coordinates * quadrants

# Let f(N) be the number of points with integer coordinates that are on a circle passing through (0,0), (N,0),(0,N), and (N,N).
def second_f(radius):
    mid_point = radius * (1 / sqrt(2))
    x = 1
    y = sqrt(radius**2 - x**2)
    integer_coordinates = 0
    quadrants = 4
    while x <= mid_point:
        if y % 1 == 0:
            integer_coordinates += 1
            # print("{}".format((x, y)))
        x += 1
        y = sqrt(radius**2 - x**2)
    return ((integer_coordinates * 2) + 1) * quadrants  # The + 1 is for the coordinate that where y = 0


def f(radius, first_coords):
    mid_point = radius * (1 / sqrt(2))
    x = 1
    y = sqrt(radius**2 - x**2)
    integer_coordinates = 0
    quadrants = 4
    coord_list = []
    while x <= mid_point:
        if y % 1 == 0:
            integer_coordinates += 1
            coord_list.append((x, y))
            # print("{}".format((x, y)))
        x += 1
        y = sqrt(radius**2 - x**2)
    # if radius % 5 == 0:
    len_coords = len(coord_list)
    # if len_coords == first_coords[len_coords]:
    #     print('|', end='')
    if first_coords[len_coords] == 0:
        first_coords[len_coords] = radius
        # print("New max coord cnt {}".format(first_coords))
        #print("{: <15} {}".format(radius, coord_list))
        print("{}".format(first_coords))
    return ((integer_coordinates * 2) + 1) * quadrants  # The + 1 is for the coordinate that where y = 0

# assert original_f(10000) == 36
# assert f(10000) == 36

def main():
    ignore_set = set()
    answer_set = set()
    for x in range(2, 10**7):
        if x not in ignore_set:
            coords = f(x)
            if coords == 4:
                # print("ignoring multiples of {}".format(x))
                i = 1
                while x < 10**7:
                    ignore_set.add(x)
                    i += 1
                    x = x**i

            else:
                if coords == 420:
                    print("Adding {} to answer set".format(x))
                    answer_set.add(x)
        else:
            print("{} was in ignore set. size of ignore set {} size of answer set {}".format(x, len(ignore_set), len(answer_set)))

    print(answer_set)
    print(sum(answer_set))


def speed_test():
    start = time.time()
    print(f(10**7))
    end = time.time()
    print("Took %f ms" % ((end - start) * 1000.0))
    # original f is taking 22500 ms for f(10**7)
    # second f gets this time down to around 7650 ms


def find_patterns():
    answer_set = set()
    first_coord = [0] * (52 + 1)
    for x in range(2, 10**7):
        coords = f(x, first_coord)
        if coords == 420:
            print("Adding {} to answer set".format(x))
            answer_set.add(x)

    print(answer_set)
    print(sum(answer_set))
    # discovered that ignoring x**i is NOT the way to add to ignore, this doesn't capture enough
    # Should do the following:  lets say 5 were the number we want to ignore the multiples of
    # Note:  This goes only to 10**3, would need to change this to 10**11 for the problem.
    # ignore_set.add(set(range(5,10**3,5)))
    # This won't actually work though, looking closer it appears whenever 5**n value is hit, the pattern shifts
    # and there's some unexplainable numbers like 65 and 85 which have 4 integers
    # need to remember I'm adding a 1 to whatever the (value * 2) is then * 4 to get the true number of integer coords
    # so to find 420 that would be ( 52 + 1 ) * 4, so we're looking for 104 hits

# |||New max coord cnt [1]
# 5               [(3, 4.0)]
# |||||New max coord cnt [2]
# 25              [(7, 24.0), (15, 20.0)]
# |New max coord cnt [4]
# 65              [(16, 63.0), (25, 60.0), (33, 56.0), (39, 52.0)]
# |||||||||||||New max coord cnt [7]
# 325             [(36, 323.0), (80, 315.0), (91, 312.0), (125, 300.0), (165, 280.0), (195, 260.0), (204, 253.0)]
# ||||||||New max coord cnt [13]
# 1105            [(47, 1104.0), (105, 1100.0), (169, 1092.0), (264, 1073.0), (272, 1071.0), (425, 1020.0), (468, 1001.0), (520, 975.0), (561, 952.0), (576, 943.0), (663, 884.0), (700, 855.0), (744, 817.0)]
# |||||||||||||||||||New max coord cnt [22]
# 5525            [(235, 5520.0), (525, 5500.0), (612, 5491.0), (845, 5460.0), (1036, 5427.0), (1131, 5408.0), (1320, 5365.0), (1360, 5355.0), (1547, 5304.0), (2044, 5133.0), (2125, 5100.0), (2163, 5084.0), (2340, 5005.0), (2600, 4875.0), (2805, 4760.0), (2880, 4715.0), (3124, 4557.0), (3315, 4420.0), (3468, 4301.0), (3500, 4275.0), (3720, 4085.0), (3861, 3952.0)]


n = 325
# first_coord = [0]*(52+1)
# print(first_coord)
#
# print(f(n, first_coord))
# print(f(n*(10-1), first_coord))
# print(f(n*10, first_coord))
# print(f(n*10*(10-1), first_coord))
# print(f(n*10*10, first_coord))
# print(f(n*(10**15), first_coord))

find_patterns()

# matches = {}
# for n in range(420, 10**11):
#     fn = f(n)
#     # print("n {} fn {}".format(n, fn))
#     if fn == 420:
#         print("Found {} Matches {}".format(n, matches))
#         matches.add(n)
#         break
#
# print(matches)
# print(sum(matches))

# [2, 5, 25, 125, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [2, 5, 25, 125, 65, 0, 0, 325, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [2, 5, 25, 125, 65, 0, 0, 325, 0, 0, 0, 0, 0, 1105, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [2, 5, 25, 125, 65, 0, 0, 325, 0, 0, 1625, 0, 0, 1105, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [2, 5, 25, 125, 65, 3125, 0, 325, 0, 0, 1625, 0, 0, 1105, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [2, 5, 25, 125, 65, 3125, 0, 325, 0, 0, 1625, 0, 4225, 1105, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [2, 5, 25, 125, 65, 3125, 0, 325, 0, 0, 1625, 0, 4225, 1105, 0, 0, 0, 0, 0, 0, 0, 0, 5525, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [2, 5, 25, 125, 65, 3125, 15625, 325, 0, 0, 1625, 0, 4225, 1105, 0, 0, 0, 0, 0, 0, 0, 0, 5525, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [2, 5, 25, 125, 65, 3125, 15625, 325, 0, 0, 1625, 0, 4225, 1105, 0, 0, 0, 21125, 0, 0, 0, 0, 5525, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [2, 5, 25, 125, 65, 3125, 15625, 325, 0, 0, 1625, 0, 4225, 1105, 0, 0, 0, 21125, 0, 0, 0, 0, 5525, 0, 0, 0, 0, 0, 0, 0, 0, 27625, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [2, 5, 25, 125, 65, 3125, 15625, 325, 0, 0, 1625, 0, 4225, 1105, 0, 0, 0, 21125, 0, 0, 0, 0, 5525, 0, 0, 0, 0, 0, 0, 0, 0, 27625, 0, 0, 0, 0, 0, 0, 0, 0, 32045, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [2, 5, 25, 125, 65, 3125, 15625, 325, 0, 0, 1625, 0, 4225, 1105, 0, 0, 40625, 21125, 0, 0, 0, 0, 5525, 0, 0, 0, 0, 0, 0, 0, 0, 27625, 0, 0, 0, 0, 0, 0, 0, 0, 32045, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [2, 5, 25, 125, 65, 3125, 15625, 325, 0, 0, 1625, 0, 4225, 1105, 0, 0, 40625, 21125, 0, 0, 0, 0, 5525, 0, 0, 0, 0, 0, 0, 0, 0, 27625, 0, 0, 0, 0, 0, 71825, 0, 0, 32045, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]