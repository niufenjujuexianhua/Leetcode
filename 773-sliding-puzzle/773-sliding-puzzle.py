class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        import collections
        s = ''
        for i in range(2):
            for j in range(3):
                s += str(board[i][j])
                if board[i][j] == 0:
                    idx = i * 3 + j

        target = '123450'
        dq = collections.deque([(s, idx, 0)])
        seen = set([s])

        while dq:
            s, idx, step = dq.popleft()

            if s == target:
                return step

            nxts = self.move(s, idx)
            for ns, nidx in nxts:
                if ns not in seen:
                    seen.add(ns)
                    dq.append((ns, nidx, step + 1))

        return -1

    def move(self, s, idx):
        nxts = []
        i, j = divmod(idx, 3)
        sls = list(s)
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 2 and 0 <= nj < 3:
                nidx = ni * 3 + nj
                sls[idx], sls[nidx] = sls[nidx], sls[idx]
                nxts.append((''.join(sls), nidx))
                sls[idx], sls[nidx] = sls[nidx], sls[idx]
        return nxts