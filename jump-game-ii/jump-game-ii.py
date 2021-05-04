class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1: return 0

        dp = [float('inf')] * n
        dp[0] = 0

        for j in range(1, n):
            for i in range(j):
                if i + nums[i] >= j:
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]