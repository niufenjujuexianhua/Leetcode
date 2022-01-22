class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        """
        :type grid: List[List[int]]
        :type pricing: List[int]
        :type start: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        i, j = start
        hq = [(0, grid[i][j], i, j)]
        seen = set([(i, j)])
        res = []
        while hq:
            d, p, i, j = heapq.heappop(hq)

            if pricing[0] <= p <= pricing[1]:
                res.append((i, j))
                if len(res) == k:
                    break

            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != 0:
                    if (ni, nj) not in seen:
                        seen.add((ni, nj))
                        heapq.heappush(hq, (d + 1, grid[ni][nj], ni, nj))



        return res