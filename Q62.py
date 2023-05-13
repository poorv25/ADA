def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[m][n], construct_lcs(dp, s1, s2)


def construct_lcs(dp, s1, s2):
    i, j = len(s1), len(s2)
    lcs = []
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(lcs))


'''The time complexity of this implementation is O(mn), where m and n are the lengths of s1 and s2, respectively. 
This is because we construct a two-dimensional array of size(m+1) x(n+1) and fill it up with values in a nested loop. 
The space complexity is also O(mn), as we need to store the two-dimensional array.
In comparison, a naive recursive implementation would have a time complexity of O(2 ^ n) and a space complexity of O(n), where n is 
the length of the shorter string. This is because the recursive algorithm would need to consider all possible subsequences, which is 
exponential in the length of the input. The dynamic programming approach is therefore much more efficient, especially for longer strings.'''
