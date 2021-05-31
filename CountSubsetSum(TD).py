wt = [2, 3, 5, 6, 8, 10]
W = 10 # sum to form
n = len(wt) # total length of numbers

# Just like knapsack we need to have a dp[n+1][W+1] matrix
# where n is the length of wts. and W is the target weight/number.
def countSubsetSum(wt, W, n):
    dp = [[0 for i in range(W+1)] for i in range(n+1)]

    # setting first row to 0 as target sum can't be achieved without any weight
    # set first column to 1 because null subset can always result in 0 as target weight
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                dp[i][j] = dp[i-1][j-wt[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][W]

print(countSubsetSum(wt, W, n))
