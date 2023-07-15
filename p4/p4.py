result = 0
# multiply each number below 1000 with each number
for i in range(1000):
    for x in range(1000):
        # check if current product is a palindrome
        if str(i * x) == str(i * x)[::-1]:
            if i * x > result:
                result = i * x

print(result)