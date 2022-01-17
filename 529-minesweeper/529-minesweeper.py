class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        for di, dj in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
        """
        m, n = len(board), len(board[0])
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        self.dfs(board, i, j)
        return board


    def dfs(self, board, i, j):
        # if board[i][j] == 'M':
        #     board[i][j] = 'X'
        #     return
        if board[i][j] != 'E':
            return

        cnt = 0
        for di, dj in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                if board[ni][nj] == 'M':
                    cnt += 1

        if cnt == 0:
            board[i][j] = 'B'
            for di, dj in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    self.dfs(board, ni, nj)
        else:
            board[i][j] = str(cnt)