class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i in [0, m - 1] or j in [0, n - 1]):
                    self.dfs(grid, i, j, m, n)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.dfs(grid, i, j, m, n)
                    res += 1

        return res

    def dfs(self, grid, i, j, m, n):
        if grid[i][j] == 1:
            return

        grid[i][j] = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                self.dfs(grid, ni, nj, m, n)