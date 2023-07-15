def is_prime(i):
    for x in range(2, i):
        if (i % x == 0):
            return False
    else:
        return True

result = []
i = 2
while len(result) < 10001:
    if is_prime(i):
        result.append(i)
    i += 1

print(result[10000])