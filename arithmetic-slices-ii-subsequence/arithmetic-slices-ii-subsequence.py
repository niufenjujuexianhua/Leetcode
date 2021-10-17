class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        total = 0 
        dp = [defaultdict(int) for _ in nums]
        
        for j in range(len(nums)):
            for i in range(j):
                diff = nums[j] - nums[i]
                dp[j][diff] += dp[i][diff] + 1 
                total += dp[i][diff]
        return total