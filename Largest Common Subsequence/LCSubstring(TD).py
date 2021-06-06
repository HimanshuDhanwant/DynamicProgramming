# Given 2 string find the longest common subsequence's length

a = 'abcdgh'
b = 'abedfha'

def lcs(s1, s2, m, n):
    dp = [[0 for i in range(n+1)] for i in range(m+1)]
    
    result = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if (s1[i-1] == s2[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0
    return result

print(lcs(a, b, len(a), len(b)))