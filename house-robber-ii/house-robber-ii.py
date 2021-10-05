class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sz = len(nums)
        if sz <= 2:
            return max(nums)

        return max(self.dfs(nums[:-1], len(nums) - 2, {}),
                   self.dfs(nums[1:], len(nums) - 2, {}))

    def dfs(self, nums, i, dp):
        if i < 0:
            return 0
        if i in dp:
            return dp[i]

        dp[i] = max(self.dfs(nums, i - 1, dp),
                    self.dfs(nums, i - 2, dp) + nums[i])
        return dp[i]
        