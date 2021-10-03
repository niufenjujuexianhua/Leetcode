class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        res = self.dfs(cost, target, {})
        return str(res) if res > 0 else '0'

    def dfs(self, cost, t, dp):
        if t == 0:
            return 0
        if t in dp:
            return dp[t]

        cur = float('-inf')
        for d in range(1, 10):
            if t >= cost[d - 1]:
                cur = max(cur,
                          self.dfs(cost, t - cost[d - 1], dp) * 10 + d)
        dp[t] = cur
        return cur
        