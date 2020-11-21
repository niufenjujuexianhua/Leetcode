# Given an array of integers nums and an integer k, return the total number of c
# ontinuous subarrays whose sum equals to k. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,1], k = 2
# Output: 2
#  Example 2: 
#  Input: nums = [1,2,3], k = 3
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 104 
#  -1000 <= nums[i] <= 1000 
#  -107 <= k <= 107 
#  
#  Related Topics Array Hash Table 
#  👍 5954 👎 201


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dt = collections.defaultdict(int)
        dt[0] = 1
        total = 0
        res = 0
        for n in nums:
            total += n
            if total - k in dt:
                res += dt[total - k]
            dt[total] += 1
        return res

        
# leetcode submit region end(Prohibit modification and deletion)
