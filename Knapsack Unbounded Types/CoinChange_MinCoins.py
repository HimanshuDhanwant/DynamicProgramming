import sys
# Minimum numbers of coins used to make a given total.

coins = [1,2,3]
total = 11

def minCoins(coins, su, n):
    dp = [[0 for i in range(su+1)] for i in range(n+1)]

    # as we are given 0 coins and to make sum >=0 we will require INF number
    # of coins. Hence initialize the row with maxsize-1
    for i in range(su+1):
        dp[0][i] = sys.maxsize-1
    
    # Exception scenario: question where we need to initialize 2nd row also.
    for i in range(1, su+1):
        if i % coins[0] == 0:
            dp[1][i] = (int)(i/coins[0])
        else:
            dp[1][i] = dp[0][i]
    
    # coding the choice diaigram
    for i in range(2, n+1):
        for j in range(1, su+1):
            if coins[i-1] <= j:
                dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][su]

print(minCoins(coins, total, len(coins)))