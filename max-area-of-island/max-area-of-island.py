class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = [0]
                    self.dfs(grid, i, j, m, n, cnt)
                    res = max(res, cnt[0])

        return res

    def dfs(self, grid, i, j, m, n, cnt):
        if grid[i][j] == 0:
            return

        cnt[0] += 1
        grid[i][j] = 0
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                self.dfs(grid, ni, nj, m, n, cnt)