# Given an integer array nums, return the number of reverse pairs in the array. 
# 
# 
#  A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 
# 2 * nums[j]. 
# 
#  
#  Example 1: 
#  Input: nums = [1,3,2,3,1]
# Output: 2
#  Example 2: 
#  Input: nums = [2,4,3,5,1]
# Output: 3
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5 * 104 
#  231 <= nums[i] <= 231 - 1 
#  
#  Related Topics Binary Search Divide and Conquer Sort Binary Indexed Tree Segm
# ent Tree 
#  👍 1354 👎 146


# leetcode submit region begin(Prohibit modification and deletion)
class BIT():
    def __init__(self, n):
        self.tree = [0] * n

    def update(self, i, delta):
        while i > 0:
            self.tree[i] += delta
            i -= i & -i

    def query(self, i):
        cnt = 0
        if i > len(self.tree):
            return cnt
        while i < len(self.tree):
            cnt += self.tree[i]
            i += i & -i
        return cnt

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums, n = sorted(nums), len(nums)
        if n == 1: return 0
        res, root = 0, BIT(n + 1)

        for num in nums:
            i = self.bs(snums, 2 * num + 1)
            res += root.query(i + 1)
            root.update(self.bs(snums, num) + 1, 1)
        return res

    def bs(self, snums, n):
        s, e = 0, len(snums) - 1
        while s + 1 < e:
            m = s + (e - s) // 2
            if snums[m] < n:
                s = m
            else:
                e = m
        if snums[s] >= n:
            return s
        if snums[e] >= n:
            return e
        return e + 1
print(Solution().reversePairs([3,2,1]))
# leetcode submit region end(Prohibit modification and deletion)
