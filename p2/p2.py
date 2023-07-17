def fib_even_smaller_than(limit):
    small, fib, result = 0, 1, 0
    while fib < limit:
        helper = fib
        fib = small + helper
        small = helper
        result += fib if fib % 2 == 0 else 0
    return result

print(fib_even_smaller_than(4000000))



