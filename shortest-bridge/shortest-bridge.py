class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        bds = set()

        i, j = self.first(grid, m, n)
        self.dfs(grid, i, j, bds, m, n)

        step = 0
        while bds:
            new = []
            for i, j in bds:
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            return step
                        elif grid[ni][nj] == 0:
                            grid[ni][nj] = -1
                            new.append((ni, nj))
            step += 1
            bds = new

    def first(self, grid, m, n):
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return i, j

    def dfs(self, grid, i, j, bds, m, n):
        # if grid[i][j] != 1:
        #     if grid[i][j] == 0:
        #         bds.append((i, j))
        #     return

        grid[i][j] = -1

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                if grid[ni][nj] == 0:
                    bds.add((i, j))
                elif grid[ni][nj] == 1:
                    self.dfs(grid, ni, nj, bds, m, n)