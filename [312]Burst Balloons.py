# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number
#  on it represented by array nums. You are asked to burst all the balloons. If th
# e you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Her
# e left and right are adjacent indices of i. After the burst, the left and right 
# then becomes adjacent. 
# 
#  Find the maximum coins you can collect by bursting the balloons wisely. 
# 
#  Note: 
# 
#  
#  You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can n
# ot burst them. 
#  0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100 
#  
# 
#  Example: 
# 
#  
# Input: [3,1,5,8]
# Output: 167 
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#  Related Topics Divide and Conquer Dynamic Programming 
#  👍 2833 👎 72


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i][j] maxn between i and j
        if not nums:
            return 0
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for j in range(1, n - 1):
            for i in range(j, 0, -1):
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k - 1] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1])
        return dp[1][n - 2]











    #     return self.dfs(nums, 1, n - 2, {})
    #
    #
    # def dfs(self, nums, i, j, memo):
    #     if i > j:
    #         return 0
    #     # if i == j:
    #     #     return nums[i - 1] * nums[i] * nums[i + 1]
    #
    #     if (i, j) in memo:
    #         return memo[(i, j)]
    #
    #     memo[(i, j)] = 0
    #     for k in range(i, j + 1):
    #         memo[(i, j)] = max(memo[(i, j)],
    #                            nums[i - 1] * nums[k] * nums[j + 1] + self.dfs(nums, i, k - 1, memo)
    #                            + self.dfs(nums, k + 1, j, memo))
    #
    #     return memo[(i, j)]

        # dp = [[0] * n for _ in range(n)]
        #
        # for j in range(1, n - 1):
        #     for i in range(j, 0, -1):
        #         for k in range(i, j + 1):
        #             dp[i][j] = max(dp[i][j],
        #                            nums[i - 1] * nums[k] * nums[j + 1] + dp[i][k - 1] + dp[k + 1][j])
        #
        # return dp[1][n - 2]

# leetcode submit region end(Prohibit modification and deletion)
