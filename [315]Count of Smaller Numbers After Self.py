# You are given an integer array nums and you have to return a new counts array.
#  The counts array has the property where counts[i] is the number of smaller elem
# ents to the right of nums[i]. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-1]
# Output: [0]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [-1,-1]
# Output: [0,0]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 105 
#  -104 <= nums[i] <= 104 
#  
#  Related Topics Binary Search Divide and Conquer Sort Binary Indexed Tree Segm
# ent Tree 
#  👍 3387 👎 106


# leetcode submit region begin(Prohibit modification and deletion)
class BIT():
    def __init__(self, n):
        self.root = [0] * n

    def update(self, i, delta):
        while i < len(self.root):
            self.root[i] += delta
            i += i & (-i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.root[i]
            i -= i & (-i)
        return res

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        root, res = BIT(n + 1), []
        rank = {v : i + 1 for i, v in enumerate(sorted(nums))}

        for n in nums[::-1]:
            r = rank[n]
            res.append(root.query(r - 1))
            root.update(r, 1)
        return res[::-1]



print(Solution().countSmaller([2,2]))

        
# leetcode submit region end(Prohibit modification and deletion)
