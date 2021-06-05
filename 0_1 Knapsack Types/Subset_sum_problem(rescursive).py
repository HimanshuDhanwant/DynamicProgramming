wt = [1, 3, 4, 5]
W = 7 # sum to form
n = len(wt) # total length of numbers

def isSubsetSum(wt, W, n):
    # base condition
    if W == 0: 
        return True 
    if (n == 0):
        return False
    
    # choice conditions / recursive calls
    if (wt[n-1] <= W):
        # return if any of (inclusion of item (OR) exlusion of item) is true
        return isSubsetSum(wt, W-wt[n-1], n-1) or isSubsetSum(wt, W, n-1)
    elif wt[n-1] > W:
        # return exclusion of item
        return isSubsetSum(wt, W, n-1)

# driver method call 
print(isSubsetSum(wt, W, n))