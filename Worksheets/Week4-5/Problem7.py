# CoffeeMagic is planning to open a series of cafes along Interstate I-99.
# There are n possible locations under consideration, and the distances of
# these locations from the start of I-99, in miles, are m1 < m2 < · · · < mn.
#
# The constraints are as follows:
#     • At most one cafe per location. Opening a cafe at location i gives profit pi to CoffeeMagic.
#     • Any two cafes must be at least k miles apart on I-99.
#
# Design a O(n)-time dynamic programming algorithm to compute the locations where
# CoffeeMagic should open cafes giving them maximum possible profit.

# p is a list of profits for each location
# m is a list of distances from the start of I-99
# k is the minimum distance between two cafes

def CoffeeMagic(p, m, k):
    dp = [0 for _ in range(len(p)+1)]
    dp[0] = 0
    dp[1] = max(p[0], 0)

    index_closest = 0

    for i in range(2, len(p)+1):
        # Update index of closest cafe,
        # increment index until the distance is less than k,
        # then grab the index right before it
        while m[i] - m[index_closest] >= k:
            index_closest += 1
        index_closest -= 1

        # Either open a cafe at i: p[i] + dp[index_closest]
        # or don't open a cafe at i: dp[i-1], the previous cafe max
        dp[i] = max(dp[i-1], dp[index_closest] + p[i])

    return dp[len(p)]
