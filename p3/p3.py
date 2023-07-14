primes = []
i = 1
factor = 1

#generate prime number
for i in range(600851475143):
    

# very inefficient
while factor < 10000000:
    
    j = 1
    # check for prime
    while i % j == 0 and (j == i or j == 1):
        factor = i
        j += 1
        print(factor)
    i += 1

    if 600851475143 % factor == 0:
        result.append(factor)

while 600851475143 % factor == 0
print(result.sort(reverse=True))
