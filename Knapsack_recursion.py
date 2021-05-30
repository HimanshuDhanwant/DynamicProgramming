wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7 # total capacity of knapsack
n = len(wt) # total length of items(wt or val)

# Method to calculate the maximum profit val given the wt array, val array, 
# max hold capacity of knapsack, length of items 
def knapsack(wt, val, W, n):
    # base condition 
    if (n == 0 or W == 0):
        return 0
    
    # choice conditions / recursive calls
    if (wt[n-1] <= W):
        # return max of (inclusion of item, exlusion of item)
        return max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
    elif wt[n-1] > W:
        # return exclusion of item
        return knapsack(wt, val, W, n-1)

# driver method call 
print(knapsack(wt, val, W, n))