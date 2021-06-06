'''
    To find maximum number of ways to make a given sum 
    given the coins of different value(unlimited in numbers).
'''

coins = [1,2,3]
su = 5

def ways(coins, S, n):
    dp = [[0 for j in range(S+1)] for i in range(n+1)]

    for i in range(n):
        dp[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, S+1):
            dp[i][j] = dp[i-1][j]
            if coins[i-1] <= j:
                # If we are asked the total no. of ways in any DP 
                # problem then, we need to add the inclusion and exclusion
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]

    return dp[n][S]

print(ways(coins, su, len(coins)))