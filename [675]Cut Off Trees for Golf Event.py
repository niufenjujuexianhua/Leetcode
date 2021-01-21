# You are asked to cut off all the trees in a forest for a golf event. The fores
# t is represented as an m x n matrix. In this matrix: 
# 
#  
#  0 means the cell cannot be walked through. 
#  1 represents an empty cell that can be walked through. 
#  A number greater than 1 represents a tree in a cell that can be walked throug
# h, and this number is the tree's height. 
#  
# 
#  In one step, you can walk in any of the four directions: north, east, south, 
# and west. If you are standing in a cell with a tree, you can choose whether to c
# ut it off. 
# 
#  You must cut off the trees in order from shortest to tallest. When you cut of
# f a tree, the value at its cell becomes 1 (an empty cell). 
# 
#  Starting from the point (0, 0), return the minimum steps you need to walk to 
# cut off all the trees. If you cannot cut off all the trees, return -1. 
# 
#  You are guaranteed that no two trees have the same height, and there is at le
# ast one tree needs to be cut off. 
# 
#  
#  Example 1: 
# 
#  
# Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
# Output: 6
# Explanation: Following the path above allows you to cut off the trees from sho
# rtest to tallest in 6 steps.
#  
# 
#  Example 2: 
# 
#  
# Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
# Output: -1
# Explanation: The trees in the bottom row cannot be accessed as the middle row 
# is blocked.
#  
# 
#  Example 3: 
# 
#  
# Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
# Output: 6
# Explanation: You can follow the same path as Example 1 to cut off all the tree
# s.
# Note that you can cut off the first tree at (0, 0) before making any steps.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == forest.length 
#  n == forest[i].length 
#  1 <= m, n <= 50 
#  0 <= forest[i][j] <= 109 
#  
#  Related Topics Breadth-first Search 
#  👍 622 👎 359


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        q = []
        m, n = len(forest), len(forest[0])
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(q, (forest[i][j], i, j))

        si, sj, step = 0, 0, 0
        while q:
            _, di, dj = heapq.heappop(q)
            moves = self.dist(si, sj, di, dj, m, n, forest)
            if moves == -1:
                return -1

            step += moves
            si, sj = di, dj
        return step

    def dist(self, si, sj, di, dj, m, n, forest):
        dq = collections.deque([(si, sj, 0)])
        seen = set([(si, sj)])
        while dq:
            i, j, moves = dq.popleft()
            if i == di and j == dj:
                return moves
            for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen and forest[ni][nj] > 0:
                    seen.add((ni, nj))
                    dq.append((ni, nj, moves + 1))
        return -1
print(Solution().cutOffTree([[1,2,3],[0,0,0],[7,6,5]]))

# leetcode submit region end(Prohibit modification and deletion)
