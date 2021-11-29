class Solution(object):
    def numIslands(self, rooms):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        res = 0 
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == '1':
                    res += 1 
                    self.bfs(rooms, m, n, i, j, 0)
                    # rooms[i][j] = dist
        return res

    def bfs(self, rooms, m, n, i, j, d):
        if not (0 <= i < m and 0 <= j < n) or rooms[i][j] == '0':
            return
        # if d > rooms[i][j]:
        #     return

        rooms[i][j] = '0'

        self.bfs(rooms, m, n, i + 1, j, d + 1)
        self.bfs(rooms, m, n, i, j + 1, d + 1)
        self.bfs(rooms, m, n, i - 1, j, d + 1)
        self.bfs(rooms, m, n, i, j - 1, d + 1)