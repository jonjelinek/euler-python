# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import sys
sys.setrecursionlimit(100000)

largest_pal = {
    'pal': 0,
    'n1': 0,
    'n2': 0,
}

def is_palindrome(num: any):
    # print("is_palindrome({})".format(num))

    if type(num) is int:
        num = str(num)

    if len(num) <= 1:
        return True

    # Use negative indexing to get last character of string [-1]
    # print("comparing {} == {}".format(num[0], num[-1]))
    if num[0] != num[-1]:
        return False
    else:
        if len(num) == 2:
            return True
        else:
            # recursively call function using inner substring
            # print("r call {}".format(num[1:-1]))
            return is_palindrome(num[1:-1])


assert is_palindrome(9009) is True
assert is_palindrome(12345) is False
assert is_palindrome(900099) is False

# start at 999 * 999 = something, is_palindrome(something) == True, if not then decrement 1 side ( might be issue here)

def find_largest_palindrome(n1, n2):
    # print("checking {} and {} ".format(n1, n2))
    if is_palindrome(n1 * n2):
        # print("found palindrome {} x {} = {}".format(n1, n2, n1*n2))
        return {
            'pal': n1*n2,
            'n1': n1,
            'n2': n2,
        }
    else:
        # print("trying {} x {}".format(n1, n2-1))
        return find_largest_palindrome(n1, n2-1)


for i in range(999,800,-1):
    tmppal = find_largest_palindrome(i, 999)
    if tmppal['pal'] > largest_pal['pal']:
        largest_pal = tmppal
    # print(largest_pal)

print("Largest Palindrome: {}".format(largest_pal))