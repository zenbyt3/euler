def multiples_of_in_range(a, b, r):
    result = 0
    for i in range(r): result += i if i % a == 0 or i % 5 == 0 else 0
    return result

print(multiples_of_in_range(3, 5, 1000))