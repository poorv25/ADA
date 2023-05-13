def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        mid = n // 2
        left_factorial = factorial(mid)
        right_factorial = factorial(n - mid)
        return left_factorial * right_factorial
