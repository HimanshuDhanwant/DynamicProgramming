import sys

arr = [1, 6, 11, 5]

# the idea is to take 2 subsets and minimize there total.
# to achieve this we will minimize the diff which is equal 
# to sum-(2*j)
# where j is the index of first half of last row of subset sum dp matrix

def findMin(arr, n):
    su = 0
    su = sum(arr)
    dp = [[False for i in range(su+1)] for j in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1, n+1):
        for j in range(1, su+1):
            dp[i][j] = dp[i-1][j]

            if (arr[i-1] <= j):
                dp[i][j] |= dp[i-1][j-arr[i-1]]

    diff = sys.maxsize
    for j in range(su // 2, -1, -1):
        if dp[n][j]:
            diff = su - (2*j)
            break
    return diff

print(findMin(arr, len(arr)))