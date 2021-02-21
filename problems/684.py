# Inverse Digit Sum

# s(n) is the smallest digit sum for n
# then function S(k) is the sum of n = 1 to k of s(n)
# finally the fibonacci thing

# s(n)
import time


def find_smallest_digit_sum(n):
     return int(str(n % 9) + '9' * (n // 9))


def find_smallest_digit_sum_without_str(n):
    print(n)
    nines = n // 9
    leading_number = n % 9
    # num_str = str(leading_number)
    num = 0
    # this is considerably slower than using string
    for x in range(nines):
        num += 10**x * 9
        # num_str += "9"
    if leading_number != 0:
        num += 10**nines * leading_number
    return num % ((10**9)+7)


assert find_smallest_digit_sum(10) == 19


def summation_of_digit_sums(k):
    sum = 0
    for n in range(k):
        sum += find_smallest_digit_sum(n + 1)
    return sum


assert summation_of_digit_sums(20) == 1074


def fib(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    previous_fi = 0
    fi = 1
    for n in range(i - 1):
        temp = fi
        fi = fi + previous_fi
        previous_fi = temp
    return fi


assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(12) == 144


# result in (10**9)+7
sum = 0
for fi in range(2, 90 + 1):
    start_time = time.time()
    n = fib(fi)
    mod_sum = int(str(n % 9) + '9' * (n // 9)) % ((10**9) + 7)
    end_time = time.time()
    print("fi %i find_smallest_digit_sum %f ms" % (fi, (end_time - start_time) * 1000.0))
    sum += mod_sum
    print("fi {} mod_sum {} sum {}".format(fi, mod_sum, sum))
print(sum)
