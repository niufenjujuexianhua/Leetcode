# Given an integer array nums and a positive integer k, return the most competit
# ive subsequence of nums of size k. 
# 
#  An array's subsequence is a self.resulting sequence obtained by erasing some (poss
# ibly zero) elements from the array. 
# 
#  We define that a subsequence a is more competitive than a subsequence b (of t
# he same length) if in the first position where a and b differ, subsequence a has
#  a number less than the corself.responding number in b. For example, [1,3,4] is more 
# competitive than [1,3,5] because the first position they differ is at the final 
# number, and 4 is less than 5. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,5,2,6], k = 2
# Output: [2,6]
# Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6]
# , [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,4,3,3,5,4,9,6], k = 4
# Output: [2,3,3,4]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 105 
#  0 <= nums[i] <= 109 
#  1 <= k <= nums.length 
#  
#  Related Topics Stack Greedy 
#  👍 168 👎 7


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stk = []
        for i, n in enumerate(nums):
            while stk and stk[-1] > n and len(stk) + len(nums) - i - 1 >= k:
                stk.pop()
            stk.append(n)
        return stk[:k]
        
# leetcode submit region end(Prohibit modification and deletion)
