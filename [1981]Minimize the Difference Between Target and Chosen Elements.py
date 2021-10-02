# You are given an m x n integer matrix mat and an integer target. 
# 
#  Choose one integer from each row in the matrix such that the absolute differe
# nce between target and the sum of the chosen elements is minimized. 
# 
#  Return the minimum absolute difference. 
# 
#  The absolute difference between two numbers a and b is the absolute value of 
# a - b. 
# 
#  
#  Example 1: 
# 
#  
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
# Output: 0
# Explanation: One possible choice is to:
# - Choose 1 from the first row.
# - Choose 5 from the second row.
# - Choose 7 from the third row.
# The sum of the chosen elements is 13, which equals the target, so the absolute
#  difference is 0.
#  
# 
#  Example 2: 
# 
#  
# Input: mat = [[1],[2],[3]], target = 100
# Output: 94
# Explanation: The best possible choice is to:
# - Choose 1 from the first row.
# - Choose 2 from the second row.
# - Choose 3 from the third row.
# The sum of the chosen elements is 6, and the absolute difference is 94.
#  
# 
#  Example 3: 
# 
#  
# Input: mat = [[1,2,9,8,7]], target = 6
# Output: 1
# Explanation: The best choice is to choose 7 from the first row.
# The absolute difference is 1.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 70 
#  1 <= mat[i][j] <= 70 
#  1 <= target <= 800 
#  
#  Related Topics Array Dynamic Programming Matrix 
#  👍 287 👎 70


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        caps = set(mat[0])

        for row in mat[1:]:
            tmp = set()
            great = - 1
            for x in caps:
                for y in row:
                    if x + y <= target:
                        tmp.add(x + y)
                    elif great == -1 or x + y < great:
                        great = x + y
            caps = tmp
            if great != -1:
                caps.add(great)

        return min([abs(cap - target) for cap in caps])
        
# leetcode submit region end(Prohibit modification and deletion)
