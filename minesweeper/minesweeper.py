class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        self.dfs(board, click)
        return board 
        
        
    def dfs(self, board, click):
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return
        
        if board[i][j] not in ['X', 'E']:
            return


        cnt = 0
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == 'M':
                cnt += 1

        if board[i][j] == 'E':
            if cnt == 0:
                board[i][j] = 'B'
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] in ['M', 'E']:
                        self.dfs(board, (ni, nj))
            else:
                board[i][j] = str(cnt)
                return 