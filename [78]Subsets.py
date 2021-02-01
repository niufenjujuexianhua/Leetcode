# Given an integer array nums of unique elements, return all possible subsets (t
# he power set). 
# 
#  The solution set must not contain duplicate subsets. Return the solution in a
# ny order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0]
# Output: [[],[0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  All the numbers of nums are unique. 
#  
#  Related Topics Array Backtracking Bit Manipulation 
#  👍 5170 👎 109


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.bt(nums, 0, res, [])
        return res

    def bt(self, nums, i, res, path):
        res.append(path[:])
        for j in range(i, len(nums)):
            self.bt(nums, j + 1, res, path + [nums[j]])

        
# leetcode submit region end(Prohibit modification and deletion)
