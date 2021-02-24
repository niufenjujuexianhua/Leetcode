# Remember the story of Little Match Girl? By now, you know exactly what matchst
# icks the little match girl has, please find out a way you can make one square by
#  using up all those matchsticks. You should not break any stick, but you can lin
# k them up, and each matchstick must be used exactly one time. 
# 
#  Your input will be several matchsticks the girl has, represented with their s
# tick length. Your output will either be true or false, to represent whether you 
# could make one square using all the matchsticks the little match girl has. 
# 
#  Example 1: 
#  
# Input: [1,1,2,2,2]
# Output: true
# 
# Explanation: You can form a square with length 2, one side of the square came 
# two sticks with length 1.
#  
#  
# 
#  Example 2: 
#  
# Input: [3,3,3,3,4]
# Output: false
# 
# Explanation: You cannot find a way to form a square with all the matchsticks.
#  
#  
# 
#  Note: 
#  
#  The length sum of the given matchsticks is in the range of 0 to 10^9.
#  The length of the given matchstick array will not exceed 15. 
#  
#  Related Topics Depth-first Search 
#  👍 732 👎 63


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 4 != 0 or len(nums) <= 3:
            return False

        total //= 4
        nums.sort(reverse = True)
        if nums[0] > total:
            return False

        return self.dfs(nums, 0, 0, total, total, {})

    def dfs(self, nums, mask, side, size, target, memo):
        if size == 0:
            return self.dfs(nums, mask, side + 1, target, target, memo)
        if side == 4:
            return True

        if mask in memo:
            return memo[mask]

        for i in range(len(nums)):
            if not mask & (1 << i) and nums[i] <= size:
                if self.dfs(nums, mask | (1 << i), side, size - nums[i], target, memo):
                    memo[mask] = True
                    return True
        memo[mask] = False
        return False
        
# leetcode submit region end(Prohibit modification and deletion)
