class Solution(object):
    def findDiagonalOrder(self, grid):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        import collections
        m, n = len(grid), len(grid[0])
        res = []

        bf = collections.deque([(0, 0)])
        step = 1
        while bf:
            sz = len(bf)
            step += 1
            seen = set()
            res.append([])
            for _ in range(sz):
                i, j = bf.popleft()
                res[-1].append(grid[i][j])

                for di, dj in [[1, 0], [0, 1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if (ni, nj) not in seen:
                            seen.add((ni, nj))
                            bf.append((ni, nj))

            # if step % 2 == 0:
            #     bf.reverse()
            # else:
            #     bf.append((ni, nj))
        ans = []
        for i, ls in enumerate(res):
            if i % 2 == 1:
                ls.reverse()
            ans.extend(ls)
        return ans 