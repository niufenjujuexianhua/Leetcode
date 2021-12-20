class Solution(object):
    def reachableNodes(self, edges, maxMoves, n):
        """
        :type edges: List[List[int]]
        :type maxMoves: int
        :type n: int
        :rtype: int
        """
        import collections
        import heapq
        g = collections.defaultdict(dict)
        for a, b, w in edges:
            g[a][b] = w + 1
            g[b][a] = w + 1

        hq = [(0, 0)]
        dist = {}

        while hq:
            moves, node = heapq.heappop(hq)
            if node in dist:
                continue
            dist[node] = moves

            for nxt in g[node]:
                if nxt not in dist and moves + g[node][nxt] <= maxMoves:
                    heapq.heappush(hq, (moves + g[node][nxt], nxt))

        res = 0
        for a, b, w in edges:
            # if a not in dist or b not in dist:
            #     continue
            ua = maxMoves - dist[a] if a in dist else 0
            ub = maxMoves - dist[b] if b in dist else 0
            res += min(w, ua + ub)
        return res + len(dist)