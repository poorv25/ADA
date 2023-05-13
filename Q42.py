def fibonacci(n):
    if n <= 1:
        return n
    else:
        if n % 2 == 0:
            half = fibonacci(n // 2)
            return half * (2 * fibonacci(n // 2 + 1) - half)
        else:
            a = fibonacci((n + 1) // 2)
            b = fibonacci((n - 1) // 2)
            return a * a + b * b
