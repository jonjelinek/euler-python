# special pythagorean triplet

# There exists exactly one pythagorean triplet for which a + b + c = 1000
# given the triplet 3 4 5, 3^2 + 4^2 = 5^2, 9 + 16 = 25
# in this example a + b + c = 12
from math import sqrt
import random

a = 150
b = 151
c = 0
total = a + b + c
while a + b + c != 1000:
    c = sqrt(a ** 2 + b ** 2)
    total = a + b + c
    if total > 1000:
        b -= 1
        if a == b:
            a -= random.randint(1, 100)
            b += random.randint(1, 100)
    else:
        if total < 1000:
            a += 1
            if a == b:
                b += random.randint(1, 100)
                a -= random.randint(1, 100)

    print("a {} b {} c {} total {}".format(a, b, c, a + b + c))
    if a + b + c == 1000:
        print("Found solution at a {} b {}, product is: {}".format( a, b, a * b * int(c)))
        break

