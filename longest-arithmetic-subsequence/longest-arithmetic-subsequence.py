class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0

        for j in range(1, n):
            for i in range(j):
                d = nums[j] - nums[i]
                dp[j][d] = dp[i][d] + 1
                res = max(res, dp[j][d])
        return res + 1