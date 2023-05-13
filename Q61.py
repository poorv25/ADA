def fibonacci(n):
    if n <= 1:
        return n

    fib = [0] * (n+1)
    fib[0], fib[1] = 0, 1

    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n]


'''The time complexity of this implementation is O(n), where n is the input parameter.
 This is because we iterate through the loop n-1 times to fill the fib array.
In comparison, the time complexity of a recursive implementation of the Fibonacci sequence is exponential(O(2 ^ n)). 
This is because the recursive function will make multiple calls to itself, each time with an input parameter that is reduced by 1 or 2. 
As a result, the number of function calls grows exponentially with the input size, making the time complexity exponential. 
Dynamic programming overcomes this issue by storing intermediate results in an array, allowing us to avoid redundant function calls 
and reducing the time complexity to linear.'''
