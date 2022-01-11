class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m, n = len(board), len(board[0])

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        self.dfs(board, click[0], click[1])
        return board

    def dfs(self, board, i, j):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] != 'E':
            return

        cnt = 0
        for di, dj in [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == 'M':
                cnt += 1

        if cnt == 0:
            board[i][j] = 'B'
            for di, dj in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
                ni, nj = i + di, j + dj
                self.dfs(board, ni, nj)
        else:
            board[i][j] = str(cnt)
            return