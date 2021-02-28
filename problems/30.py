# digit fifth powers

values = set()
power = 5
n = 2
last_hit = 0
while (n - last_hit) < 10**6:
    s = str(n)
    _sum = 0
    for c in s:
        _sum += (int(c)**power)
    if _sum == n:
        # print(n, last_hit)
        values.add(n)
        last_hit = n
    n += 1

print(values)
print("Solution: {}".format(sum(values)))