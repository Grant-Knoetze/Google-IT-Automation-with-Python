# Fibonacci numbers module

def fib(n):
    """Print fibonacci series
    up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(890)


def fib2(n):
    """Return fibonacci series
    up to n, return result in
    a list"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


