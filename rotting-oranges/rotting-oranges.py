class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import collections
        m, n = len(grid), len(grid[0])
        rotten = set()
        fresh = set()
        freshcnt = 0 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                    freshcnt += 1 
                elif grid[i][j] == 2:
                    rotten.add((i, j))
        
        if freshcnt == 0:
            return 0 
        
        res = 0
        for i, j in fresh:
            days = self.bfs(grid, i, j, m, n, rotten)
            if days == -1:
                return -1 
            res = max(res, days)
        return res

    def bfs(self, grid, i, j, m, n, rotten):
        bf = collections.deque([(i, j, 0)])
        seen = set([(i, j)])

        while bf:
            i, j, days = bf.popleft()
            if (i, j) in rotten:
                return days

            for ni, nj in ((i-1,j),(i,j-1),(i,j+1),(i+1,j)):
                # ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] != 0:
                        if (ni, nj) not in seen:
                            seen.add((ni, nj))
                            bf.append((ni, nj, days + 1))
        return -1 