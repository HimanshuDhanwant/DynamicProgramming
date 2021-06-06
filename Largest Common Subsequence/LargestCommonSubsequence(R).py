# Given 2 string find the longest common subsequence's length

a = 'abcdgh'
b = 'abedfha'

def lcs(s1, s2, idx_1, idx_2):
    if idx_1 == 0 or idx_2 == 0:
        return 0
    
    if s1[idx_1-1] == s2[idx_2-1]:
        return 1 + lcs(s1, s2, idx_1-1, idx_2-1)
    else:
        return max(lcs(s1, s2, idx_1, idx_2-1), lcs(s1, s2, idx_1-1, idx_2))

print(lcs(a, b, len(a), len(b)))