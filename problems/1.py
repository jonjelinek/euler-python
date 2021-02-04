# Problem 1 - Multiples of 3 and 5 https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def getSumOfMultiplesInRange(multiples: list, stop_at: int):
    nums = []
    for multiple in multiples:
        # Remember range() does not include the last/stop_at value
        nums += range(multiple, stop_at, multiple)
        print(nums)

    # convert to set to only contain unique values, then convert back to list
    nums = list(set(nums))
    return sum(nums)

assert 23 == getSumOfMultiplesInRange([3,5], 10)
print(getSumOfMultiplesInRange([3,5], 1000))