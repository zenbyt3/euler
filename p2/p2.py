small = 1
big = 1
helper = 0
result = 0
while big < 4000000:
    helper = big
    big = big + small
    small = helper
    if big % 2 == 0:
        result += big
    print(small)
print(result)