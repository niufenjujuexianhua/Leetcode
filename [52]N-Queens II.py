# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other. 
# 
#  Given an integer n, return the number of distinct solutions to the n-queens p
# uzzle. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 9 
#  
#  Related Topics Backtracking 
#  👍 740 👎 176


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.bt(0, [], n)
        return self.res

    def bt(self, row, cols, n):
        if row == n:
            self.res += 1
            return

        for col in range(n):
            if self.valid(cols, row, col):
                self.bt(row + 1, cols + [col], n)

    def valid(self, cols, row, col):
        for i in range(row):
            if i - cols[i] == row - col or i + cols[i] == row + col or cols[i] == col:
                return False
        return True
        
# leetcode submit region end(Prohibit modification and deletion)
