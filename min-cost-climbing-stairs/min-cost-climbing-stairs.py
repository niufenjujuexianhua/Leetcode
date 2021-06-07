class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        return self.dfs(cost, len(cost), {})

    def dfs(self, cost, i, m):
        if i <= 1:
            return 0
        if i in m:
            return m[i]

        m[i] = min(self.dfs(cost, i - 2, m) + cost[i - 2],
                   self.dfs(cost, i - 1, m) + cost[i - 1])
        return m[i]