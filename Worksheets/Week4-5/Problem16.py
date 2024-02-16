## Problem 16 (Longest Wiggly Subsequence).
#
# A sequence of distinct integers (a1, . . . , ak ) is called wiggly 
# if a1 < a2 > a3 < a4 · · · and so on. More formally, ai < ai +1
# whenever i is odd and ai > ai +1 whenever i is even. Given an array A[1 : n] of
# distinct integers, design an efficient algorithm to find the longest wiggly 
# subsequence. 
# 
# An O(n2) time algorithm will suffice.

def longest_wiggly(A):
    dp = [[0, 0] for _ in range(len(A)+1)] # dp[i][0] ends UP, dp[i][1] ends DOWN
    dp[1] = [1, 1]

    for i in range(1, len(A)+1):
        for j in range(i):
            if A[i-1] > A[j-1]: # Case 1, if have a pair that go UP, lets update UP 
                dp[i][0] = max(dp[i][0], dp[j][1]+1) # Use either the current best UP or the best DOWN + 1
            if A[i-1] < A[j-1]: 
                dp[i][1] = max(dp[i][1], dp[j][0]+1)

    return max(dp[len(A)]) # Return the max of ending UP or ending DOWN

