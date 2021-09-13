class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = max(nums)
        dp = [0] * (mx + 1)
        freq = collections.Counter(nums)

        for i in range(1, mx + 1):
            rob = dp[i - 2] + freq[i] * i if i >= 2 else freq[i] * i
            notrob = dp[i - 1]
            dp[i] = max(rob, notrob)

        return dp[-1]