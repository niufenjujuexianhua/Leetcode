class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        import collections
        import heapq
        g = collections.defaultdict(dict)

        for s, e, t in times:
            g[s][e] = t

        seen = {}
        # seen[k] = 0
        hq = [(0, k)]

        while hq:
            time, node = heapq.heappop(hq)
            if node in seen:
                continue

            seen[node] = time

            for nxt in g[node]:
                if nxt not in seen:
                    heapq.heappush(hq, (time + g[node][nxt], nxt))

        if len(seen) < n:
            return -1
        return max(seen.values())