class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        import heapq
        m, n = len(grid), len(grid[0])
        free = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '#':
                    free.add((i, j))
                if grid[i][j] == 'B':
                    box = (i, j)
                if grid[i][j] == 'T':
                    target = (i ,j)
                if grid[i][j] == 'S':
                    person = (i, j)

        hq = [(0, person, box)]
        seen = set()

        while hq:
            step, p, b = heapq.heappop(hq)
            if b == target:
                return step

            if (p, b) in seen:
                continue
            seen.add((p, b))

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                np = (p[0] + di, p[1] + dj)
                nb = (b[0] + di, b[1] + dj)

                # if np in free and nb in free:
                #     if np == b:
                #         heapq.heappush(hq, (step + 1, np, nb))
                #     elif np != b:
                #         heapq.heappush(hq, (step, np, b))
                if np == b and nb in free:
                    heapq.heappush(hq, (step + 1, np, nb))
                elif np in free and np != b:
                    heapq.heappush(hq, (step, np, b))

        return -1