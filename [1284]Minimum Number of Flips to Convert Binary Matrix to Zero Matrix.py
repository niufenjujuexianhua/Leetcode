# Given a m x n binary matrix mat. In one step, you can choose one cell and flip
#  it and all the four neighbours of it if they exist (Flip is changing 1 to 0 and
#  0 to 1). A pair of cells are called neighboors if they share one edge. 
# 
#  Return the minimum number of steps required to convert mat to a zero matrix o
# r -1 if you cannot. 
# 
#  Binary matrix is a matrix with all cells equal to 0 or 1 only. 
# 
#  Zero matrix is a matrix with all cells equal to 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: mat = [[0,0],[0,1]]
# Output: 3
# Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (
# 1, 1) as shown.
#  
# 
#  Example 2: 
# 
#  
# Input: mat = [[0]]
# Output: 0
# Explanation: Given matrix is a zero matrix. We don't need to change it.
#  
# 
#  Example 3: 
# 
#  
# Input: mat = [[1,1,1],[1,0,1],[0,0,0]]
# Output: 6
#  
# 
#  Example 4: 
# 
#  
# Input: mat = [[1,0,0],[1,0,0]]
# Output: -1
# Explanation: Given matrix can't be a zero matrix
#  
# 
#  
#  Constraints: 
# 
#  
#  m == mat.length 
#  n == mat[0].length 
#  1 <= m <= 3 
#  1 <= n <= 3 
#  mat[i][j] is 0 or 1. 
#  
#  Related Topics Breadth-first Search 
#  👍 260 👎 30


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        import collections
        m, n = len(mat), len(mat[0])
        ls = sum(mat, [])
        dq = collections.deque([(ls, 0)])
        seen = set([tuple(ls)])

        while dq:
            node, step = dq.popleft()

            if sum(node) == 0:
                return step

            for x in range(m):
                for y in range(n):
                    tmp = node[:]
                    self.flip(tmp, x, y, m, n)

                    if tuple(tmp) not in seen:
                        seen.add(tuple(tmp))
                        dq.append((tmp, step + 1))
        return -1
        
    def flip(self, ls, x, y, m, n):
        ls[x * n + y] = 1 - ls[x * n + y]
        for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                # print(nx, ny, m, n, ls)
                ls[nx * n + ny] = 1 - ls[nx * n + ny]
print(Solution().minFlips([[0],[1],[1]]))
# leetcode submit region end(Prohibit modification and deletion)
