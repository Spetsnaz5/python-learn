def fib(n):    # write Fibonacci series less than n
    """
    Print a Fibonacci series less than n.
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)


def fib2(t):
    return t

for i in range(5):
    x, y = fib2((i, i**2))
    print(x, y)
    
