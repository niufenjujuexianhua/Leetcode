# You are given a sorted array consisting of only integers where every element a
# ppears exactly twice, except for one element which appears exactly once. Find th
# is single element that appears only once. 
# 
#  Follow up: Your solution should run in O(log n) time and O(1) space. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
#  Example 2: 
#  Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10^5 
#  0 <= nums[i] <= 10^5 
#  Related Topics Binary Search 
#  👍 1988 👎 83


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, e = 0, len(nums) - 1
        while s + 1 < e:
            m = s + (e - s) // 2

            if m % 2 == 0:
                if nums[m] == nums[m + 1]:
                    s = m
                else:
                    e = m
            else:
                if nums[m] == nums[m - 1]:
                    s = m
                else:
                    e = m
        if s % 2 == 0: return nums[s]
        return nums[e]
        
# leetcode submit region end(Prohibit modification and deletion)
