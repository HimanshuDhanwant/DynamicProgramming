a = 'heap'
b = 'pea'

# str1 and str2 be the given strings.
# m and n be their lengths respectively.
# len be the length of the longest common subsequence of str1 and str2
# minimum number of deletions minDel = m – len
# minimum number of Insertions minInsert = n – len

def lcs(s1, s2, m, n):
    dp = [[0 for i in range(n+1)] for i in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if (s1[i-1] == s2[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def minOperations(a, b, m, n):
    lcs_size = lcs(a, b, m, n)
    return (m-lcs_size) + (n-lcs_size)

print(minOperations(a, b, len(a), len(b)))
