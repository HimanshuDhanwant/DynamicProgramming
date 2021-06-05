'''
Given a rod of length n inches and an array of prices that includes prices of all pieces of size 
smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces
'''

def cutRod(wt, val, W, n):
    dp = [[0 for j in range(W+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            if(wt[i-1] <= j):
                dp[i][j] = max(dp[i-1][j], val[i-1] + dp[i][j-wt[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]

# Driver code
W = 8 # Total length of rod
val = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(val)
print("Maximum Obtainable Value is", cutRod([i for i in range(1, size+1)], val, W, size))