class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])

        for i, j in hits:
            grid[i][j] -= 1

        for j in range(n):
            self.dfs(grid, 0, j)

        res = [0] * len(hits)
        for idx in reversed(range(len(hits))):
            i, j = hits[idx]
            grid[i][j] += 1
            if grid[i][j] == 1 and self.is_connected(grid, i, j):
                res[idx] = self.dfs(grid, i, j) - 1

        return res

    def is_connected(self, grid, i, j):
        if grid[i][j] == 2 or i == 0:
            return True
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 2:
                return True
        return False

    def dfs(self, grid, i, j):
        if grid[i][j] != 1:
            return 0

        grid[i][j] = 2
        res = 1

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                res += self.dfs(grid, ni, nj)
        return res