class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        import heapq
        state, k = 0, 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].islower():
                    # state |= (1 << (ord(grid[i][j]) - ord('a')))
                    k += 1

        q = [(0, start[0], start[1], 0)]
        seen = {(start[0], start[1], 0) : 0}
        while q:
            steps, x, y, state = heapq.heappop(q)
            # print(q)

            if state == (1 << k) - 1:
                return steps

            for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#':
                    if grid[nx][ny].isupper() and not (state & (1 << (ord(grid[nx][ny].lower()) - ord('a')))):
                        continue
                    ns = state | (1 << (ord(grid[nx][ny].lower()) - ord('a'))) if ord(grid[nx][ny].lower()) >= ord('a') else state
                    # if grid[nx][ny].islower():
                    #     ns |= (1 << (ord(grid[nx][ny]) - ord('a')))
                    # if (nx, ny, ns) not in seen:
                    #     if 'a' <= grid[nx][ny] <= 'f':
                    #         seen[(nx, ny, ns)] = steps + 1
                    #         heapq.heappush(q, (steps + 1, nx, ny, ns))
                    #     elif 'A' <= grid[nx][ny] <= 'F' and not (ns & 1 << (ord(grid[nx][ny].lower()) - ord('a'))):
                    #         seen[(nx, ny, ns)] = steps + 1
                    #         heapq.heappush(q, (steps + 1, nx, ny, ns))
                    #     elif grid[nx][ny] == '.':
                    if (nx, ny, ns) not in seen:
                        seen[(nx, ny, ns)] = steps + 1
                        heapq.heappush(q, (steps + 1, nx, ny, ns))

        return -1
print(Solution().shortestPathAllKeys(["@abcdeABCDEFf"]))
        
