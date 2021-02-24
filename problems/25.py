# 1000 digit fibonacci number


previous_fi = 0
fvalue = 1
findex = 1  # findex: 0 = 0, 1 = 1, 2 = 1, 3 = 2, ...
while True:
    findex += 1
    temp = fvalue
    fvalue = fvalue + previous_fi
    previous_fi = temp
    if len(str(fvalue)) == 1000:
        break

print("Fib index {} is first fib number of length {}.  value: {}".format(findex, len(str(fvalue)), fvalue))
