# Given an m x n matrix of non-negative integers representing the height of each
#  unit cell in a continent, the "Pacific ocean" touches the left and top edges of
#  the matrix and the "Atlantic ocean" touches the right and bottom edges. 
# 
#  Water can only flow in four directions (up, down, left, or right) from a cell
#  to another one with height equal or lower. 
# 
#  Find the list of grid coordinates where water can flow to both the Pacific an
# d Atlantic ocean. 
# 
#  Note: 
# 
#  
#  The order of returned grid coordinates does not matter. 
#  Both m and n are less than 150. 
#  
# 
#  
# 
#  Example: 
# 
#  
# Given the following 5x5 matrix:
# 
#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with paren
# theses in above matrix).
#  
# 
#  
#  Related Topics Depth-first Search Breadth-first Search 
#  👍 1695 👎 389


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        aq, pq = collections.deque([]), collections.deque([])
        aseen, pseen = set(), set()
        for i in range(m):
            pq.append((i, 0))
            aq.append((i, n - 1))
            pseen.add((i, 0))
            aseen.add((i, n - 1))
        for j in range(n):
            pq.append((0, j))
            aq.append((m - 1, j))
            pseen.add((0, j))
            aseen.add((m - 1, j))

        return self.bfs(aq, aseen, matrix, m, n) & self.bfs(pq, pseen, matrix, m, n)

    def bfs(self, q, seen, grid, m, n):
        while q:
            x, y = q.popleft()
            for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] >= grid[x][y] and (nx, ny) not in seen:
                    q.append((nx, ny))
                    seen.add((nx, ny))
        return seen

        
# leetcode submit region end(Prohibit modification and deletion)
