class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        n = len(slices) // 3 
        return max(self.dp(slices[1:], n),
                   self.dp(slices[:-1], n))
        
    
    def dp(self, slices, n):
        dp = [[0] * (n + 1) for _ in range(len(slices) + 1)]
        
        for s in range(1, len(slices) + 1):
            for k in range(1, n + 1):
                dp[s][k] = max(slices[s - 1] + (dp[s - 2][k - 1] if s >= 2 else 0),
                                dp[s - 1][k])
        
        return max(dp[-1])