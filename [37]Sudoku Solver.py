# Write a program to solve a Sudoku puzzle by filling the empty cells. 
# 
#  A sudoku solution must satisfy all of the following rules: 
# 
#  
#  Each of the digits 1-9 must occur exactly once in each row. 
#  Each of the digits 1-9 must occur exactly once in each column. 
#  Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes
#  of the grid. 
#  
# 
#  The '.' character indicates empty cells. 
# 
#  
#  Example 1: 
# 
#  
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5"
# ,".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".","."
# ,".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".","."
# ,"6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"
# ],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4
# ","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3
# "],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],[
# "9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3",
# "4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is sho
# wn below:
# 
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  board.length == 9 
#  board[i].length == 9 
#  board[i][j] is a digit or '.'. 
#  It is guaranteed that the input board has only one solution. 
#  
#  Related Topics Hash Table Backtracking 
#  👍 2489 👎 100


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveSudoku(self, board):
        from collections import defaultdict
        rdt, cdt, bdt = defaultdict(set), defaultdict(set), defaultdict(set)
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    rdt[i].add(board[i][j])
                    cdt[j].add(board[i][j])
                    bdt[(i // 3, j // 3)].add(board[i][j])

        self.bt(board, empty, rdt, cdt, bdt)
        return board

    def bt(self, board, empty, rdt, cdt, bdt):
        if not empty:
            return True

        i, j = empty[-1]
        for n in map(str, list(range(1, 10))):
            if n not in rdt[i] and n not in cdt[j] and n not in bdt[(i // 3, j // 3)]:
                empty.pop()
                rdt[i].add(n)
                cdt[j].add(n)
                bdt[(i // 3, j // 3)].add(n)
                board[i][j] = n

                if self.bt(board, empty, rdt, cdt, bdt):
                    return True

                empty.append((i, j))
                rdt[i].remove(n)
                cdt[j].remove(n)
                bdt[(i // 3, j // 3)].remove(n)
                board[i][j] = '.'

        return False

        
# leetcode submit region end(Prohibit modification and deletion)
