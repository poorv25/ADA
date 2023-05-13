def lcs(X, Y):
    # Find lengths of two strings
    m = len(X)
    n = len(Y)

    # Initialize the memoization table
    L = [[None] * (n + 1) for i in range(m + 1)]

    # Fill the memoization table in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # return the length of LCS
    return L[m][n]
