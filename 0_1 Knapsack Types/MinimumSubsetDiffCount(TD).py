arr = [1, 1, 2, 3]
diff = 1

'''
    let the sum of 2 subset(scooped out of given subset) be S1 and S2.
    As diff is given and sum of S can calculated...
        S1 - S2 = diff
        S1 + S2 = sum
    By solving both, we can conclude
        S1 = (diff + sum)/2
    Hence, S1 as W(total weight of knapsack) in count of subset sum can 
    give us the desired output.
'''

def countOfSubsetSum(arr, W, n):
    dp = [[0 for i in range(W+1)] for j in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, W+1):
            dp[i][j] = dp[i-1][j]

            if (arr[i-1] <= j):
                dp[i][j] += dp[i-1][j-arr[i-1]]
    return dp[n][W]

def countMin(arr, diff):
    su = (diff + sum(arr))//2
    return countOfSubsetSum(arr, su, len(arr))

print(countMin(arr, diff))