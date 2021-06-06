# Given 2 string find the longest common subsequence's length
# USING MEMOIZATION

a = 'abcdgh'
b = 'abedfha'

dp = [[-1 for i in range(len(b)+1)] for i in range(len(a)+1)]

def lcs(s1, s2, idx_1, idx_2):
    if idx_1 == 0 or idx_2 == 0:
        return 0

    if (dp[idx_1][idx_2] != -1):
        return dp[idx_1][idx_2]
    
    if s1[idx_1-1] == s2[idx_2-1]:
        dp[idx_1][idx_2] = 1 + lcs(s1, s2, idx_1-1, idx_2-1)
        return dp[idx_1][idx_2]
    else:
        dp[idx_1][idx_2] = max(lcs(s1, s2, idx_1, idx_2-1), lcs(s1, s2, idx_1-1, idx_2))
        return dp[idx_1][idx_2]

print(lcs(a, b, len(a), len(b)))