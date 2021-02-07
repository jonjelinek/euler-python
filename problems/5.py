# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time
import sys
sys.setrecursionlimit(100000)

# def get_number_divisible_by_range(num, r):
#     for divisor in r:
#         # print("divisor {} num {}".format(divisor, num))
#         if num % divisor != 0:
#             return get_number_divisible_by_range(num + r[-1], r)
#     return num

def get_number_divisible_by_range(num, r):
    for divisor in r:
        # print("divisor {} num {}".format(divisor, num))
        if num % divisor != 0:
            return False
    return num

def smallest_num_divisible_by_range(r):
    # step by the largest number, check if each smaller num is divisible, if not, step
    num = 0
    answer = False
    while answer is False:
        answer = get_number_divisible_by_range(num + r[-1], r)
        num += r[-1]
    return answer


start = 1
stop = 10
step = 1
stop += step
assert 2520 == smallest_num_divisible_by_range(range(start, stop, step))

start_time = time.time()
start = 1
stop = 20
step = 1
stop += step
print(smallest_num_divisible_by_range(range(start, stop, step)))
end_time = time.time()
print(f"Runtime {end_time - start_time}")