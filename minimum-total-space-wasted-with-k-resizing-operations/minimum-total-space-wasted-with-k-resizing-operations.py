class Solution(object):
    def minSpaceWastedKResizing(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.dfs(nums, 0, k, {})

    def dfs(self, nums, i, k, dp):
        if i == len(nums):
            return 0
        if k < 0:
            return float('inf')
        if (i, k) in dp:
            return dp[(i, k)]

        ans = float('inf')
        total = 0
        mx = float('-inf')
        for j in range(i, len(nums)):
            mx = max(mx, nums[j])
            total += nums[j]
            ans = min(ans, self.dfs(nums, j + 1, k - 1, dp) + mx * (j - i + 1) - total)
        dp[(i, k)] = ans
        return ans