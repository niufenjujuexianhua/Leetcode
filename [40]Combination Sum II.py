# Given a collection of candidate numbers (candidates) and a target number (targ
# et), find all unique combinations in candidates where the candidate numbers sum 
# to target. 
# 
#  Each number in candidates may only be used once in the combination. 
# 
#  Note: The solution set must not contain duplicate combinations. 
# 
#  
#  Example 1: 
# 
#  
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
#  Related Topics Array Backtracking 
#  👍 2456 👎 85


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum2(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.bt(sorted(nums), 0, target, [], res)
        return res

    def bt(self, nums, i, target, path, res):
        if target <= 0:
            if target == 0:
                res.append(path)
            return

        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]: continue
            self.bt(nums, j + 1, target - nums[j], path + [nums[j]], res)
        
# leetcode submit region end(Prohibit modification and deletion)
