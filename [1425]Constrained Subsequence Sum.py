# Given an integer array nums and an integer k, return the maximum sum of a non-
# empty subsequence of that array such that for every two consecutive integers in 
# the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is s
# atisfied. 
# 
#  A subsequence of an array is obtained by deleting some number of elements (ca
# n be zero) from the array, leaving the remaining elements in their original orde
# r. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest numbe
# r.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= nums.length <= 105 
#  -104 <= nums[i] <= 104 
#  
#  Related Topics Dynamic Programming 
#  👍 437 👎 21


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        res = float('-inf')
        dq = collections.deque([])

        for i, n in enumerate(nums):
            while dq and i - dq[0][0] > k:
                dq.popleft()
            tmp = max(n, n + (dq[0][1] if dq else 0))
            while dq and tmp >= dq[-1][1]:
                dq.pop()
            res = max(res, tmp)
            dq.append((i, tmp))
        return res
# print(Solution().constrainedSubsetSum([10,2,-10,5,20], 2))
# leetcode submit region end(Prohibit modification and deletion)
