# Given an integer array nums that may contain duplicates, return all possible s
# ubsets (the power set). 
# 
#  The solution set must not contain duplicate subsets. Return the solution in a
# ny order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#  Example 2: 
#  Input: nums = [0]
# Output: [[],[0]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
#  Related Topics Array Backtracking 
#  👍 2217 👎 99


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        self.bt(sorted(nums), 0, res, [])
        return res

    def bt(self, nums, i, res, path):
        res.append(path[:])
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            self.bt(nums, j + 1, res, path + [nums[j]])

# leetcode submit region end(Prohibit modification and deletion)
