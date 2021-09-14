class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        res = [float('inf')]
        bits = 0

        for i in range(m):
            for j in range(n):
                bits |= mat[i][j] << (i * n + j)

        seen = set([bits])
        bfs = collections.deque([[bits, 0]])

        while bfs:
            bits, step = bfs.popleft()

            if bits == 0:
                return step

            for i in range(m):
                for j in range(n):
                    nxt = bits
                    for di, dj in [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            nxt ^= 1 << (ni * n + nj)

                    if nxt not in seen:
                        seen.add(nxt)
                        bfs.append([nxt, step + 1])
        return -1