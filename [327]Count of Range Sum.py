# Given an integer array nums and two integers lower and upper, return the numbe
# r of range sums that lie in [lower, upper] inclusive. 
# 
#  Range sum S(i, j) is defined as the sum of the elements in nums between indic
# es i and j inclusive, where i <= j. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respectiv
# e sums are: -2, -1, 2.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0], lower = 0, upper = 0
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  -231 <= nums[i] <= 231 - 1 
#  -3 * 104 <= lower <= upper <= 3 * 104 
#  
# 
#  
# Follow up: A naive algorithm of O(n2) is trivial, Could you do better than tha
# t? Related Topics Binary Search Divide and Conquer Sort Binary Indexed Tree Segm
# ent Tree 
#  👍 1032 👎 120


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1] + n)

        import collections
        record = collections.defaultdict(int)

        res = 0
        for csum in cumsum:
            for target in range(lower, upper + 1):
                if csum - target in record:
                    res += record[csum - target]
            record[csum] += 1
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
