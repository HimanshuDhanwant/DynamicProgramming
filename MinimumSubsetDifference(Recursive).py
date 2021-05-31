# partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
wt = [1, 7, 11, 6]

def minDiff(wt, i, calculatedSum, totalSum):
    # base condition when the last element is remaining in the array 
    # and this gives the diff of two subsets
    # which further is used in recursive calls to min sum of 2 subsets
    if i == 0:
        return abs((totalSum - calculatedSum) - calculatedSum)

    # below calculates the minimum of calculatedSum with element included and excluded
    return min(minDiff(wt, i-1, calculatedSum + wt[i-1], totalSum), minDiff(wt, i-1, calculatedSum, totalSum))


def main():
    sum = 0 
    for w in wt:
        sum += w
    print(minDiff(wt, len(wt), 0, sum))

main()