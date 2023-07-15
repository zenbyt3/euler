#generate prime number
num = 600851475143

#generate prime number
for i in range(2, num):
    for x in range(2, i):
        if (i % x == 0):
            break
    else:
        # check if num is divisible by factor i
        if num % i == 0:
            print(i)
