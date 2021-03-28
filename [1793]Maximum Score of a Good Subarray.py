# You are given an array of integers nums (0-indexed) and an integer k. 
# 
#  The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., num
# s[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j. 
# 
#  Return the maximum possible score of a good subarray. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,4,3,7,4,5], k = 3
# Output: 15
# Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (
# 5-1+1) = 3 * 5 = 15. 
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [5,5,4,5,4,1,1,1], k = 0
# Output: 20
# Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (
# 4-0+1) = 4 * 5 = 20.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 2 * 104 
#  0 <= k < nums.length 
#  
#  Related Topics Greedy 
#  👍 217 👎 14


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumScore(self, nums, k):
        # i = j = k
        # res = minn = nums[k]
        # n = len(nums)
        #
        # while i > 0 or j < n - 1:
        #     if (nums[i - 1] if i else 0) < (nums[j + 1] if j < n - 1 else 0):
        #         j += 1
        #     else:
        #         i -= 1
        #     minn = min(minn, nums[i], nums[j])
        #     res = max(res, minn * (j - i + 1))
        # return res

        stack = []
        res = 0
        nums.append(0)
        for i, h in enumerate(nums):
            while stack and h <= nums[stack[-1]]:
                curh = nums[stack.pop()]
                if (not stack or stack[-1] < k) and i > k:
                    width = i - stack[-1] - 1 if stack else i
                    res = max(res, curh * width)
            stack.append(i)
        return res





print(Solution().maximumScore([6569,9667,3148,7698,1622,2194,793,9041,1670,1872],
5))
# leetcode submit region end(Prohibit modification and deletion)
