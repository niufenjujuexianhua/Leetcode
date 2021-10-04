class Solution(object):
    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ss, n = sum(nums), len(nums)
        return any(self.dfs(nums, 0, k, ss * k // n, {}) for k in range(1, n // 2 + 1) if ss * k % n == 0)

    def dfs(self, nums, i, k, target, dp):
        if k == 0:
            return target == 0
        if target < 0 or len(nums) - i < k:
            return False

        if (target, k, i) in dp:
            return dp[(target, k, i)]

        dp[(target, k, i)] = self.dfs(nums, i + 1, k - 1, target - nums[i], dp) or \
                             self.dfs(nums, i + 1, k, target, dp)
        return dp[(target, k, i)]