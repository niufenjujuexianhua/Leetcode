# 
# Given a circular array (the next element of the last element is the first elem
# ent of the array), print the Next Greater Number for every element. The Next Gre
# ater Number of a number x is the first greater number to its traversing-order ne
# xt in the array, which means you could search circularly to find its next greate
# r number. If it doesn't exist, output -1 for this number.
#  
# 
#  Example 1: 
#  
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find n
# ext greater number; The second 1's next greater number needs to search circularl
# y, which is also 2.
#  
#  
# 
#  Note:
# The length of given array won't exceed 10000.
#  Related Topics Stack 
#  👍 1905 👎 82


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dt, stack = {}, []
        n = len(nums)
        res = [-1] * n

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            # reduce time
            if i < n:
                stack.append(i % n)

        return res

# print(Solution().nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100]))

    # leetcode submit region end(Prohibit modification and deletion)
