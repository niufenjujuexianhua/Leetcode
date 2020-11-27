# Given an integer array, your task is to find all the different possible increa
# sing subsequences of the given array, and the length of an increasing subsequenc
# e should be at least 2. 
# 
#  
# 
#  Example: 
# 
#  
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4
# ,7,7]]
#  
# 
#  
#  Constraints: 
# 
#  
#  The length of the given array will not exceed 15. 
#  The range of integer in the given array is [-100,100]. 
#  The given array may contain duplicates, and two equal integers should also be
#  considered as a special case of increasing sequence. 
#  
#  Related Topics Depth-first Search 
#  👍 846 👎 128


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        self.bt(nums, 0, res, ())
        return res

    def bt(self, nums, i, res, path):
        if len(path) >= 2:
            res.add(path[:])

        for j in range(i, len(nums)):
            if not path or path[-1] <= nums[j]:
                self.bt(nums, j + 1, res, path + (nums[j],))

# print(Solution().findSubsequences([4,6,7,7]))
# leetcode submit region end(Prohibit modification and deletion)
