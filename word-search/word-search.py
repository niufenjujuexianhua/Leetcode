class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        memo = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0, memo):
                    return True
        return False

    def dfs(self, board, i, j, word, k, memo):
        if k == len(word):
            return True
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return False
        if board[i][j] != word[k] or board[i][j] == '#':
            return False

        tmp = board[i][j]
        board[i][j] = '#'
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if self.dfs(board, ni, nj, word, k + 1, memo):
                return True
        board[i][j] = tmp
        return False