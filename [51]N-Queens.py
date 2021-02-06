# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other. 
# 
#  Given an integer n, return all distinct solutions to the n-queens puzzle. 
# 
#  Each solution contains a distinct board configuration of the n-queens' placem
# ent, where 'Q' and '.' both indicate a queen and an empty space, respectively. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as show
# n above
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: [["Q"]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 9 
#  
#  Related Topics Backtracking 
#  👍 2609 👎 96


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        grid = [['.'] * n for _ in range(n)]
        self.bt(grid, 0, set(), set(), set(), n, res)
        return res

    def bt(self, grid, row, cols, diag, adiag, n, res):
        if row == n:
            res.append([''.join(row) for row in grid])
            return

        for col in range(n):
            if not (col in cols or (row - col) in diag or (row + col) in adiag):
                grid[row][col] = 'Q'
                cols.add(col)
                diag.add(row - col)
                adiag.add(row + col)

                self.bt(grid, row + 1, cols, diag, adiag, n, res)
                
                grid[row][col] = '.'
                cols.remove(col)
                diag.remove(row - col)
                adiag.remove(row + col)



#     def valid(self, taken, row, col, n):
#         if taken & (1 << (n - col - 1)): return False
#
#         for i in reversed(range(row)):
#             if col != n - 1 and taken & (1 << (n - (row + col - i) - 1)): return False
#             if col != 0 and taken & (1 << (n - (row - col + i) - 1)): return False
#         return True
# print(Solution().solveNQueens(4))
# leetcode submit region end(Prohibit modification and deletion)
