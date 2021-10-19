class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        total = 0

        for j in range(1, n):
            for i in range(j):
                d = nums[j] - nums[i]
                dp[j][d] += dp[i][d] + 1
                total += dp[i][d]
        return total