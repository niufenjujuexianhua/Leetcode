# We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is
#  the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks. 
# 
#  We start at the starting point, and one move consists of walking one space in
#  one of the 4 cardinal directions. We cannot walk outside the grid, or walk into
#  a wall. If we walk over a key, we pick it up. We can't walk over a lock unless 
# we have the corresponding key. 
# 
#  For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter
#  of the first K letters of the English alphabet in the grid. This means that the
# re is exactly one key for each lock, and one lock for each key; and also that th
# e letters used to represent the keys and locks were chosen in the same order as 
# the English alphabet. 
# 
#  Return the lowest number of moves to acquire all keys. If it's impossible, re
# turn -1. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["@.a.#","###.#","b.A.B"]
# Output: 8
#  
# 
#  
#  Example 2: 
# 
#  
# Input: ["@..aA","..B#.","....b"]
# Output: 6
#  
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= grid.length <= 30 
#  1 <= grid[0].length <= 30 
#  grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F' 
#  The number of keys is in [1, 6]. Each key has a different letter and opens ex
# actly one lock. 
#  
#  
#  Related Topics Heap Breadth-first Search 
#  👍 489 👎 19


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestPathAllKeys(self, grid):
        import heapq
        k = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].islower():
                    k += 1

        q = [(0, start[0], start[1], 0)]
        seen = {(start[0], start[1], 0)}
        while q:
            steps, x, y, state = heapq.heappop(q)

            if state == (1 << k) - 1:
                return steps

            for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#':
                    if grid[nx][ny].isupper() and not (state & (1 << (ord(grid[nx][ny].lower()) - ord('a')))):
                        continue
                    ns = state | (1 << (ord(grid[nx][ny].lower()) - ord('a'))) if ord(grid[nx][ny].lower()) >= ord('a') else state
                    if (nx, ny, ns) not in seen:
                        seen.add((nx, ny, ns))
                        heapq.heappush(q, (steps + 1, nx, ny, ns))
        return -1
# print(Solution().shortestPathAllKeys(["@abcdeABCDEFf"]))
        
# leetcode submit region end(Prohibit modification and deletion)
