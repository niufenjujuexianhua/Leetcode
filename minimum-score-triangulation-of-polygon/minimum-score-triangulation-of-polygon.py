class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        sz = len(values)
        dp = [[0] * sz for _ in range(sz)]
        return self.dfs(values, 0, sz - 1, dp)

    def dfs(self, values, i, j, dp):
        if dp[i][j] != 0:
            return dp[i][j]
        if j - i < 2:
            return 0
        
        res = float('inf')
        for k in range(i + 1, j):
            cur = values[i] * values[k] * values[j]
            res = min(res,
                      cur + self.dfs(values, i, k, dp) + self.dfs(values, k, j, dp))

        dp[i][j] = res
        return res