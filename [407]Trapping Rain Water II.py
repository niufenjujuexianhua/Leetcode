# Given an m x n matrix of positive integers representing the height of each uni
# t cell in a 2D elevation map, compute the volume of water it is able to trap aft
# er raining. 
# 
#  Example: 
# 
#  
# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]
# 
# Return 4.
#  
# 
#  
# 
#  The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,
# 3,3,2,3,1]] before the rain. 
# 
#  
# 
#  
# 
#  After the rain, water is trapped between the blocks. The total volume of wate
# r trapped is 4. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= m, n <= 110 
#  0 <= heightMap[i][j] <= 20000 
#  
#  Related Topics Heap Breadth-first Search 
#  👍 1658 👎 37


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        seen, q, m, n = set([]), [], len(heightMap), len(heightMap[0])

        for i in range(m):
            heapq.heappush(q, (heightMap[i][0], i, 0))
            heapq.heappush(q, (heightMap[i][n - 1], i, n - 1))
            seen.add((i, 0))
            seen.add((i, n - 1))
        for j in range(1, n - 1):
            heapq.heappush(q, (heightMap[0][j], 0, j))
            heapq.heappush(q, (heightMap[m - 1][j], m - 1, j))
            seen.add((0, j))
            seen.add((m - 1, j))

        maxh, res = 0, 0
        while q:
            h, x, y = heapq.heappop(q)
            maxh = max(maxh, h)

            for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                    if heightMap[nx][ny] < maxh:
                        res += maxh - heightMap[nx][ny]
                        heightMap[nx][ny] = maxh
                    seen.add((nx, ny))
                    heapq.heappush(q, (heightMap[nx][ny], nx, ny))
        return res





        
# leetcode submit region end(Prohibit modification and deletion)
