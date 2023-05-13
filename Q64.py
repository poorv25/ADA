def rod_cutting(n, prices):
    # Initialize the table for storing solutions
    table = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            max_val = max(max_val, prices[j] + table[i - j - 1])
        table[i] = max_val
    
    return table[n]
