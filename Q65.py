def matrix_chain_order(p):
    n = len(p)-1
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i+length-1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m[0][n-1], s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i+1}", end='')
    else:
        print("(", end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j]+1, j)
        print(")", end='')

p = [30, 35, 15, 5, 10, 20, 25]
cost, solution = matrix_chain_order(p)
print("Optimal Parenthesization: ", end='')
print_optimal_parens(solution, 0, len(p)-2)
