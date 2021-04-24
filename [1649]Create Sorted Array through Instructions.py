# Given an integer array instructions, you are asked to create a sorted array fr
# om the elements in instructions. You start with an empty container nums. For eac
# h element from left to right in instructions, insert it into nums. The cost of e
# ach insertion is the minimum of the following: 
# 
#  
#  The number of elements currently in nums that are strictly less than instruct
# ions[i]. 
#  The number of elements currently in nums that are strictly greater than instr
# uctions[i]. 
#  
# 
#  For example, if inserting element 3 into nums = [1,2,3,5], the cost of insert
# ion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3)
#  and nums will become [1,2,3,3,5]. 
# 
#  Return the total cost to insert all elements from instructions into nums. Sin
# ce the answer may be large, return it modulo 109 + 7 
# 
#  
#  Example 1: 
# 
#  
# Input: instructions = [1,5,6,2]
# Output: 1
# Explanation: Begin with nums = [].
# Insert 1 with cost min(0, 0) = 0, now nums = [1].
# Insert 5 with cost min(1, 0) = 0, now nums = [1,5].
# Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6].
# Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6].
# The total cost is 0 + 0 + 0 + 1 = 1. 
# 
#  Example 2: 
# 
#  
# Input: instructions = [1,2,3,6,5,4]
# Output: 3
# Explanation: Begin with nums = [].
# Insert 1 with cost min(0, 0) = 0, now nums = [1].
# Insert 2 with cost min(1, 0) = 0, now nums = [1,2].
# Insert 3 with cost min(2, 0) = 0, now nums = [1,2,3].
# Insert 6 with cost min(3, 0) = 0, now nums = [1,2,3,6].
# Insert 5 with cost min(3, 1) = 1, now nums = [1,2,3,5,6].
# Insert 4 with cost min(3, 2) = 2, now nums = [1,2,3,4,5,6].
# The total cost is 0 + 0 + 0 + 0 + 1 + 2 = 3.
#  
# 
#  Example 3: 
# 
#  
# Input: instructions = [1,3,3,3,2,4,2,1,2]
# Output: 4
# Explanation: Begin with nums = [].
# Insert 1 with cost min(0, 0) = 0, now nums = [1].
# Insert 3 with cost min(1, 0) = 0, now nums = [1,3].
# Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3].
# Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3,3].
# Insert 2 with cost min(1, 3) = 1, now nums = [1,2,3,3,3].
# Insert 4 with cost min(5, 0) = 0, now nums = [1,2,3,3,3,4].
# ​​​​​​​Insert 2 with cost min(1, 4) = 1, now nums = [1,2,2,3,3,3,4].
# ​​​​​​​Insert 1 with cost min(0, 6) = 0, now nums = [1,1,2,2,3,3,3,4].
# ​​​​​​​Insert 2 with cost min(2, 4) = 2, now nums = [1,1,2,2,2,3,3,3,4].
# The total cost is 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= instructions.length <= 105 
#  1 <= instructions[i] <= 105 
#  Related Topics Binary Search Binary Indexed Tree Segment Tree Ordered Map 
#  👍 349 👎 50


# leetcode submit region begin(Prohibit modification and deletion)
class BIT():
    def __init__(self, n):
        self.tree = [0] * n

    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        cnt = 0
        while i > 0:
            cnt += self.tree[i]
            i -= i & -i
        return cnt


class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        root = BIT(max(instructions) + 1)

        res = 0
        for i, n in enumerate(instructions):
            res += min(root.query(n - 1), i - root.query(n))
            root.update(n, 1)
        return res % (10 ** 9 + 7)
        



# leetcode submit region end(Prohibit modification and deletion)
