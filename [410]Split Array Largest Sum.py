# Given an array nums which consists of non-negative integers and an integer m, 
# you can split the array into m non-empty continuous subarrays. 
# 
#  Write an algorithm to minimize the largest sum among these m subarrays. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,4,4], m = 3
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 1000 
#  0 <= nums[i] <= 106 
#  1 <= m <= min(50, nums.length) 
#  
#  Related Topics Binary Search Dynamic Programming 
#  👍 2502 👎 92


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        s, e = max(nums), sum(nums)
        while s + 1 < e:
            mid = s + (e - s) // 2
            if self.canSplit(nums, mid, m):
                e = mid
            else:
                s = mid

        if self.canSplit(nums, s, m):
            return s
        return e

    def canSplit(self, nums, mid, m):
        cnt, sm = 1, 0
        for n in nums:
            if n > mid: return False
            if sm + n <= mid:
                sm += n
            else:
                sm = n
                cnt += 1
        return cnt <= m
 # leetcode submit region end(Prohibit modification and deletion)
