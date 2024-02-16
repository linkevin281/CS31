# Problem 18: Rod Cutting Redux
# You have metal rod which is n units long. In the market,
# a rod of length i units sells for pi dollars, for integer 1 ≤ i ≤ n.
# So, you want to cut this rod into pieces to maximize sales. You may not
# assume that pi ’s are increasing; in particular, certain pi could be 0
# (for instance, no one may want a length 13 rod). cutting the rod costs
# money as well. Your cutting equipment is such that making a cut anywhere
# on a length i rod costs you ci dollars. Your goal is to figure out a way
# of cutting the rod and selling the pieces made so as to maximize the total
# profit: sales minus.
#
# Design an O(n2) time algorithm for the above problem.


# n is the length of the rod
# p is the price of the rod at length i
# c is the cost of cutting the rod at length i
def rod_cutting_redux(n, p, c):
    dp = [0 for _ in range(n+1)]
    cuts = [[] for _ in range(n+1)]
    dp[0] = 0
    dp[1] = p[0]

    # For each len of rod
    for i in range(2, n+1):
        # Check all cuts on rod len i
        final_max = p[i]
        for j in range(1, i+1):
            # dp[i] is the max of p[i], selling the rod itself
            #                  or dp[j] + p[i-j] - c[i], selling the rod j and i-j,
            #                       two rods cut from a rod of i.
            dp[i] = max(p[i], dp[j] + p[i-j] - c[i])
        if final_max != p[i]:
            cuts[i] = [j, i-j]
        else:
            cuts[i] = [i]

    path = backtrace(cuts, n)
    for i in range(len(path)-1, -1, -1):
        if len(path[i]) == 2:
            print(f'Cut rod of length {sum(path[i])} into rods of length {path[i][0]} and {path[i][1]}')
        else:
            print(f'Sell rod of length {path[i][0]}')

    return dp[n]


def backtrace(cuts, n):
    path = []
    index = n
    if n == 0:
        return path

    # Lets walk backwards until we get to the length 0 rod
    while index > 0:
        path.append(cuts[index]) # append the cut, this contains the length of both rods 
        index -= cuts[index][0]  # cuts[index][0] is either the length of the rod sold, 
                                 # or the length of the first rod from the cut, which is the 
                                 # dp based rod
    return path
