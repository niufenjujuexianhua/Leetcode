# Given an array of n integers nums, a 132 pattern is a subsequence of three int
# egers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < n
# ums[j]. 
# 
#  Return true if there is a 132 pattern in nums, otherwise, return false. 
# 
#  Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the
#  O(n) solution? 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3,
#  0] and [-1, 2, 0].
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 104 
#  -109 <= nums[i] <= 109 
#  
#  Related Topics Stack 
#  👍 1997 👎 128


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stk = []
        s3 = -float('inf')

        for i in reversed(range(len(nums))):
            n = nums[i]

            if n < s3:
                return True

            while stk and n > stk[-1]:
                s3 = stk.pop()
            stk.append(n)

        return False


# print(Solution().find132pattern([3,5,0,3,4]))

        
# leetcode submit region end(Prohibit modification and deletion)
