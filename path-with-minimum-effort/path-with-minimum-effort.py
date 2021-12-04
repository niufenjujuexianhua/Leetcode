class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        mn, mx = float('inf'), float('-inf')
        m, n = len(heights), len(heights[0])

        seen = [[float('inf')] * n for _ in range(m)]
        hq = [[0, 0, 0]]

        while hq:
            cost, i, j = heapq.heappop(hq)
            if cost > seen[i][j]:
                continue
            if i == m - 1 and j == n - 1:
                return cost

            # seen[i][j] = min(seen[i][j], cost)

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    nd = max(cost, abs(heights[ni][nj] - heights[i][j]))
                    if nd < seen[ni][nj]:
                    # if seen[ni][nj] == float('inf'):
                    #     bf.append((ni, nj))
                    #     seen.add((ni, nj))
                        seen[ni][nj] = nd 
                        heapq.heappush(hq, (nd, ni, nj))