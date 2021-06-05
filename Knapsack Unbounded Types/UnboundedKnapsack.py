'''
    Its an unbounded knapsack problem as we can use 1 or more instances of any resource. 
    A simple 1D array, say dp[W+1] can be used such that dp[i] stores the maximum value 
    which can achieved using all items and i capacity of knapsack. 

    Note that we use 1D array here which is different from classical knapsack where we 
    used 2D array. Here number of items never changes. We always have all items available.
    We can recursively compute dp[] using below formula

    1. Initialising dp[] array by 0.
    2. Implementing dp[i] = max(dp[i], val[j] + dp[i-wt[j]])
    3. Result = dp[W]
'''

def unboundedKnapsack2D(wt, val, W, n):
    dp = [[0 for j in range(W+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            if(wt[i-1] <= j):
                dp[i][j] = max(dp[i-1][j], val[i-1] + dp[i][j-wt[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]

# def unboundedKnapsack(arr, val, W, n):
#     dp = [0] * (W+1)

#     for i in range(W+1):
#         for j in range(n):
#             if (arr[j] <= i):
#                 dp[i] = max(dp[i], val[j] + dp[i - arr[j]])

#     return dp[W]

# Driver program
W = 100
val = [10, 30, 20]
wt = [5, 10, 15]

print(unboundedKnapsack2D(wt, val, W, len(wt)))