class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    1 2 3
    4 5 6
    7 8 9
    dp[i][j] = costs[i][j] + min(dp[i - 1][k] k != j)
    """

    def minCostII(self, costs):
        # write your code here
        if not costs or len(costs) == 0:
            return 0
        n, k = len(costs), len(costs[0])
        if n == 0:
            return 0

        min1 = min2 = 0
        dp = [0] * k

        for i in range(n):
            omin1, omin2 = min1, min2
            min1 = min2 = float('inf')

            for j in range(k):
                if dp[j] != omin1 or omin1 == omin2:
                    dp[j] = omin1 + costs[i][j]
                else:
                    dp[j] = omin2 + costs[i][j]

                if min1 <= dp[j]:
                    min2 = min(min2, dp[j])
                else:
                    min2 = min1
                    min1 = dp[j]
        return min1

