wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7 # total capacity of knapsack
n = len(wt) # total length of items(wt or val)

# initializing top down matrix
dp = [[0 for j in range(W+1)] for i in range(n+1)]


for i in range(n+1):
    for j in range(W+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif (wt[i-1] <= j):
            dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][W])