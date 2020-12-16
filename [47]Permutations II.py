# Given a collection of numbers, nums, that might contain duplicates, return all
#  possible unique permutations in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
#  Related Topics Backtracking 
#  👍 2576 👎 71


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.bt(nums, [], res, set())
        return res

    def bt(self, nums, path, res, seen):
        if len(path) == len(nums):
            res.append(path[:])
            return

        last = float('inf')
        for j in range(len(nums)):
            # if j > 0 and nums[j] == nums[j - 1]: continue
            if j in seen: continue
            if nums[j] == last: continue
            last = nums[j]

            self.bt(nums, path + [nums[j]], res, seen.union(set([j])))
# print(Solution().permuteUnique([1,2,2]))
# leetcode submit region end(Prohibit modification and deletion)
