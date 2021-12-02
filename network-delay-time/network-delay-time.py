class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        g = collections.defaultdict(dict)

        for u, v, t in times:
            g[u][v] = t

        seen = [0] + [-1] * n
        # seen[k] = 0
        hq = [(0, k)]

        while hq:
            time, node = heapq.heappop(hq)
            if seen[node] != -1:
                continue 
            seen[node] = time

            for nxt in g[node]:
                if seen[nxt] == -1:
                    heapq.heappush(hq, (time + g[node][nxt], nxt))
        if -1 in seen:
            return -1
        return max(seen)