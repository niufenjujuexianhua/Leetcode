class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        p = list(range(n * n))
        rank = [1] * n * n
        zeros = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            if self.find(p, rank, i * n + j) != self.find(p, rank, ni * n + nj):
                                self.union(p, rank, i * n + j, ni * n + nj)
                else:
                    zeros.append((i, j))
        
        if not zeros:
            return n * n 
        
        res = 0
        for i, j in zeros:
            dt = {}
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                    par = self.find(p, rank, ni * n + nj)
                    dt[par] = rank[par]
            res = max(res, sum(dt.values()) + 1)
        return res

    def union(self, p, rank, a, b):
        pa = self.find(p, rank, a)
        pb = self.find(p, rank, b)

        if rank[pa] <= rank[pb]:
            p[pa] = pb
            rank[pb] += rank[pa]
        # elif rank[pa] < rank[pb]:
        #     p[pa] = pb
        #     rank[pb] += rank[pa]
        else:
            p[pb] = pa
            rank[pa] += rank[pb]

    def find(self, p, rank, a):
        if p[a] != a:
            p[a] = self.find(p, rank, p[a])
        return p[a]