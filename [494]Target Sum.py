# You are given a list of non-negative integers, a1, a2, ..., an, and a target, 
# S. Now you have 2 symbols + and -. For each integer, you should choose one from 
# + and - as its new symbol. 
# 
#  Find out how many ways to assign symbols to make sum of integers equal to tar
# get S. 
# 
#  Example 1: 
# 
#  
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  The length of the given array is positive and will not exceed 20. 
#  The sum of elements in the given array will not exceed 1000. 
#  Your output answer is guaranteed to be fitted in a 32-bit integer. 
#  
#  Related Topics Dynamic Programming Depth-first Search 
#  👍 3730 👎 150


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findTargetSumWays(self, nums, s):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.dfs(nums, 0, s, {})

    def dfs(self, nums, i, s, memo):
        if i == len(nums):
            if s == 0:
                return 1
            return 0

        if (i, s) in memo:
            return memo[(i, s)]

        memo[(i, s)] = 0
        memo[(i, s)] += self.dfs(nums, i + 1, s - nums[i], memo)
        memo[(i, s)] += self.dfs(nums, i + 1, s + nums[i], memo)

        return memo[(i, s)]
        
# leetcode submit region end(Prohibit modification and deletion)
