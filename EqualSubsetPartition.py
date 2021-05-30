# In this problem we need to find if there exists 
# subset in given set whose sum is equal 

wt = [1, 5, 11, 5]

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

def containsEqualPartition(wt):
    total = sum(wt)
    if total % 2 != 0:
        return False
    else: 
        return isSubsetSum(wt, total/2, len(wt))

# driver method call 
print(containsEqualPartition(wt))