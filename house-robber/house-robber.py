class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sz = len(nums)
        if sz == 0:
            return 0

        return self.dfs(nums, len(nums) - 1, {})


    def dfs(self, nums, i, dp):
        if i <= 1:
            return max(nums[:i + 1])
        if i in dp:
            return dp[i]

        dp[i] = max(self.dfs(nums, i - 1, dp),
                    self.dfs(nums, i - 2, dp) + nums[i])
        return dp[i]