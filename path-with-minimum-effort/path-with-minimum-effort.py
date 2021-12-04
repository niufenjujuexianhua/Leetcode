class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        mn, mx = float('inf'), float('-inf')
        m, n = len(heights), len(heights[0])

        for i in range(m):
            for j in range(n):
                mn = min(mn, heights[i][j])
                mx = max(mx, heights[i][j])

        s, e = 0, mx - mn
        while s < e:
            mid = s + (e - s) // 2
            if not self.valid(heights, mid):
                s = mid + 1
            else:
                e = mid
        return s

    def valid(self, heights, mid):
        import collections
        m, n = len(heights), len(heights[0])
        bf = collections.deque([(0, 0)])
        seen = set([(0, 0)])

        while bf:
            i, j = bf.popleft()

            if (i, j) == (m - 1, n - 1):
                return True

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if (ni, nj) not in seen and abs(heights[i][j] - heights[ni][nj]) <= mid:
                        bf.append((ni, nj))
                        seen.add((ni, nj))

        return False