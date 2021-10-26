class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {0:0}
        ss = res = 0

        for i, n in enumerate(nums):
            ss += n
            if ss - target in dp:
                res = max(res, dp[ss - target] + 1)
            dp[ss] = res
        return res
    
    
    
    