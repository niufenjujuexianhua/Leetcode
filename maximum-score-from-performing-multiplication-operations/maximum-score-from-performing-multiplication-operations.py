class Solution(object):
    def maximumScore(self, nums, mults):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        dp[i:j] = max(s[i] + dp[i+1:j], s[j] + dp[i:j-1])
        """
        dp = [[0 for x in range(len(mults))] for y in range(len(mults))] 
        return self.dfs(nums, mults, 0, 0, dp)

    def dfs(self, nums, muls, i, k, dp):
        if k == len(muls):
            return 0
        if dp[i][k]:
            return dp[i][k]
        
        j = len(nums) - 1 - (k - i)
        dp[i][k] = max(nums[i] * muls[k] + self.dfs(nums, muls, i + 1, k + 1, dp),
                         nums[j] * muls[k] + self.dfs(nums, muls, i, k + 1, dp))
        return dp[i][k]