class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.dfs(matrix, target, 0, len(matrix[0]) - 1)

    def dfs(self, matrix, target, r, c):
        if r >= len(matrix) or c < 0:
            return False

        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            return self.dfs(matrix, target, r, c - 1)
        else:
            return self.dfs(matrix, target, r + 1, c)