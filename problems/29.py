# distinct powers

values = set()

limit = 100

for a in range(2, limit + 1):
    for b in range(2, limit + 1):
        values.add(a**b)

print(len(values))