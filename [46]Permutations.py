# Given an array nums of distinct integers, return all the possible permutations
# . You can return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  Example 2: 
#  Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#  Example 3: 
#  Input: nums = [1]
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  All the integers of nums are unique. 
#  
#  Related Topics Backtracking 
#  👍 5329 👎 125


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.bt(nums, 0, [], res)
        return res

    def bt(self, nums, used, path, res):
        if used == (1 << len(nums)) - 1:
            res.append(path[:])

        for i in range(len(nums)):
            if not used & (1 << i):
                self.bt(nums, used | (1 << i), path + [nums[i]], res)

        
# leetcode submit region end(Prohibit modification and deletion)
