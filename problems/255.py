# Rounded Square Roots
import math
import time


def rounded_square_root_iterations(n):
    # Let d be the number of digits of n
    d = len(str(n))
    x = []
    if d % 2 == 0:
        # even x0 = 7 * 10^((d-2)/2))
        x.append(7 * 10**((d - 2) / 2))
    else:
        # odd  x0 = 2 * 10^((d - 1) / 2))
        x.append(2 * 10**((d - 1) / 2))

    # Perform first two iterations to having something to test for the while loop
    x.append(math.floor((x[-1] + math.ceil(n / x[-1])) / 2))
    x.append(math.floor((x[-1] + math.ceil(n / x[-1])) / 2))

    while x[-2] != x[-1]:
        x.append(math.floor((x[-1] + math.ceil(n / x[-1])) / 2))

    # For the actual rounded square root
    # return x[-1]

    # For the iterations needed to find, - 1 accounts for removing the initial even or odd x0 value
    # print("{} {}".format(n, len(x) - 1))
    return len(x) - 1


# assert rounded_square_root(4321) == 66
assert rounded_square_root_iterations(4321) == 2


def rounded_square_root_average_iterations(r):
    total = 0
    for n in r:
        # if n % 10**5 == 0:
        #     print(n, total)
        total += rounded_square_root_iterations(n)
    # print(total)
    # print(len(r))
    return format(total / (len(r) - 1), '.10f')
    # return total / (len(r) - 1)

################################


def rounded_square_root_iterations_opt_list(n, d, even):
    x = []
    if even:
        x.append(7 * 10**((d - 2) / 2))
    else:
        x.append(2 * 10**((d - 1) / 2))
    x.append(math.floor((x[-1] + math.ceil(n / x[-1])) / 2))
    x.append(math.floor((x[-1] + math.ceil(n / x[-1])) / 2))
    while x[-2] != x[-1]:
        x.append(math.floor((x[-1] + math.ceil(n / x[-1])) / 2))
    return len(x) - 1


def rounded_square_root_average_iterations_optimized_list(r):
    # Assuming all numbers will be same length for optimization, i.e. 10000 = 5 digits till 99999 = also 5 digits
    n = r[0]
    # Let d be the number of digits of n
    d = len(str(n))
    total = 0
    total = sum([rounded_square_root_iterations_opt_list(num, d, True) for num in r])
    # print(total)
    return format(total / (len(r) - 1), '.10f')

###

def rounded_square_root_average_iterations_opt_2(r):
    # Assuming all numbers will be same length for optimization, i.e. 10000 = 5 digits till 99999 = also 5 digits
    n = r[0]
    # Let d be the number of digits of n
    d = len(str(n))
    even = True if d % 2 == 0 else False
    # This accounts for the first two iterations in the for loop for all numbers
    iterations = (len(r) - 1) * 2
    # print("iterations {}".format(iterations))
    for num in r:
        x0 = (7 * 10**((d - 2) / 2)) if even else (2 * 10**((d - 1) / 2))
        previous_value = math.floor((x0 + math.ceil(num / x0)) / 2)
        current_value = math.floor((previous_value + math.ceil(num / previous_value)) / 2)
        while current_value != previous_value:
            previous_value = current_value
            current_value = math.floor((previous_value + math.ceil(num / previous_value)) / 2)
            iterations += 1
    # print("iterations {}".format(iterations))
    return format(iterations / (len(r) - 1), '.10f')

print("original")
start = time.time()
print(rounded_square_root_average_iterations(range(10**4, 10**5)))
end = time.time()
print("Took %f ms" % ((end - start) * 1000.0))
start = time.time()
print(rounded_square_root_average_iterations(range(10**5, 10**6)))
end = time.time()
print("Took %f ms" % ((end - start) * 1000.0))

print("opt list")
start = time.time()
print(rounded_square_root_average_iterations_optimized_list(range(10**4, 10**5)))
end = time.time()
print("Took %f ms" % ((end - start) * 1000.0))
start = time.time()
print(rounded_square_root_average_iterations_optimized_list(range(10**5, 10**6)))
end = time.time()
print("Took %f ms" % ((end - start) * 1000.0))

print("opt 2")
start = time.time()
print(rounded_square_root_average_iterations_opt_2(range(10**4, 10**5)))
end = time.time()
print("Took %f ms" % ((end - start) * 1000.0))
start = time.time()
print(rounded_square_root_average_iterations_opt_2(range(10**5, 10**6)))
end = time.time()
print("Took %f ms" % ((end - start) * 1000.0))

# print(rounded_square_root_average_iterations(range(10**13, 10**14)))

# assert rounded_square_root_average(range(10000, 99999 + 1)) == 3.2102888889

# 2147690530  with the + 1 and then dividing by ( len(r) -1 )
# 2147246081  without passing + 1 with the range and just dividing by len(r)
