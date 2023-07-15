result = 0
number = 1

while True:
    number += 1
    for i in range(1, 21):
        if number % i != 0:
            break

        # if we reach 20 and we didnt break out of the loop,
        # we have the number that is evenly divisible by all numbers between 1 and 20
        if i == 20:
            result = number
    if result > 0:
        break

print(result)