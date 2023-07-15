def sum_of_squares(n):
    result = []
    for i in range(1, n+1):
        result.append(i**2)
    return sum(result)

def square_of_sum(n):
    result = []
    for i in range(1, n+1):
        result.append(i)
    return sum(result)**2
  
n = 100
print(square_of_sum(n) - sum_of_squares(n))