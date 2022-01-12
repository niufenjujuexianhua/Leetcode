class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        subgrids = collections.defaultdict(set)
        cells = []

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    cells.append((i, j))
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    subgrids[(i // 3, j // 3)].add(val)

        self.dfs(board, cells, rows, cols, subgrids)
        return board

    def dfs(self, board, cells, rows, cols, subgrids):
        if not cells:
            return True

        i, j = cells.pop()
        for dig in map(str, range(1, 10)):
            if dig not in rows[i] and dig not in cols[j] and dig not in subgrids[(i // 3, j // 3)]:
                rows[i].add(dig)
                cols[j].add(dig)
                subgrids[(i // 3, j // 3)].add(dig)
                board[i][j] = dig
                # cells.pop()
                if self.dfs(board, cells, rows, cols, subgrids):
                    return True
                rows[i].remove(dig)
                cols[j].remove(dig)
                subgrids[(i // 3, j // 3)].remove(dig)
                board[i][j] = '.'
        cells.append((i, j))
        return False
