class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        res = [[float('inf')] * n for _ in range(m)]
        dq = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    # seen.add((i, j))
                    dq.append((i, j))

        while dq:
            i, j = dq.popleft()
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(mat) and 0 <= nj < len(mat[0]):
                    if res[ni][nj] > res[i][j] + 1:
                        res[ni][nj] = res[i][j] + 1
                        dq.append((ni, nj))

        return res