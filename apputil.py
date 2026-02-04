# update/add code below ...
def fibonacci(n):
    """Return the nth number of the Fibonacci Series."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
fibonacci(9)