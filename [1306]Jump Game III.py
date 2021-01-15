# Given an array of non-negative integers arr, you are initially positioned at s
# tart index of the array. When you are at index i, you can jump to i + arr[i] or 
# i - arr[i], check if you can reach to any index with value 0. 
# 
#  Notice that you can not jump outside of the array at any time. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true 
# Explanation: 
# One possible way to reach at index 3 with value 0 is: 
# index 0 -> index 4 -> index 1 -> index 3
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 5 * 104 
#  0 <= arr[i] < arr.length 
#  0 <= start < arr.length 
#  
#  Related Topics Depth-first Search Breadth-first Search Recursion 
#  👍 959 👎 30


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        return self.dfs(arr, start, len(arr), set())

    def dfs(self, arr, i, n, seen):
        if not (0 <= i < n) or i in seen:
            return False
        if arr[i] == 0:
            return True

        seen.add(i)
        if (self.dfs(arr, i + arr[i], n, seen) or
            self.dfs(arr, i - arr[i], n, seen)):
            return True
        return False

        
# leetcode submit region end(Prohibit modification and deletion)
