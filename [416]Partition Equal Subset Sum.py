# Given a non-empty array nums containing only positive integers, find if the ar
# ray can be partitioned into two subsets such that the sum of elements in both su
# bsets is equal. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
#  Related Topics Dynamic Programming 
#  👍 4011 👎 89


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0: return False

        total //= 2
        return self.bt(sorted(nums, reverse=True), 0, total, {})

    def bt(self, nums, i, total, memo):
        if total == 0:
            return True
        if total < 0 or i == len(nums):
            return False
        if (i, total) in memo:
            return memo[(i, total)]
        ans = self.bt(nums, i + 1, total - nums[i], memo) or self.bt(nums, i + 1, total, memo)
        memo[(i, total)] = ans
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
