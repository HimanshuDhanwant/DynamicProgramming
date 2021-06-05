wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7 # total capacity of knapsack
n = len(wt) # total length of items(wt or val)

# initializing memo matrix
dp = [[-1 for j in range(W+1)] for i in range(n+1)]

# Method to calculate the maximum profit val given the wt array, val array, 
# max hold capacity of knapsack, length of items 
def knapsack_memo(wt, val, W, n):
    # base condition
    if (n==0 or W==0):
        return 0
    if (dp[n][W] != -1):
        return dp[n][W]
    
    # choice conditions / recursive calls
    if (wt[n-1] <= W):
        # return max of (inclusion of item, exlusion of item)
        dp[n][W] = max(val[n-1] + knapsack_memo(wt, val, W-wt[n-1], n-1), knapsack_memo(wt, val, W, n-1))
        return dp[n][W]
    elif wt[n-1] > W:
        # return exclusion of item
        dp[n][W] = knapsack_memo(wt, val, W, n-1)
        return dp[n][W]

# driver method call 
knapsack_memo(wt, val, W, n)
print(dp[n][W])

# Time Complexity:
# Since we are avoiding duplicate calculation by storing intermediate results in a 2-D array. The time complexity, in this case, is O(N*W) where N is the number of items and W is the total weight the knapsack can hold.
# Space Complexity:
# We are creating an array of size 1001 * 1001 and hence the space complexity is O(1001*1001).