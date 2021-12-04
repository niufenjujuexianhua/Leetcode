class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        import collections
        if not flights or src == dst:
            return 0

        g = collections.defaultdict(dict)
        for s, d, p in flights:
            g[s][d] = p
        # return self.bfs(n, flights, src, dst, k)

        # res = [float('inf')]
        # self.dfs(n, flights, src, dst, -1, k, res, 0, g)
        # return res[0]if res[0] != float('inf') else -1
        # return self.dijstra(n, flights, src, dst, k, g)

        return self.bellman(n, flights, src, dst, k, g)
    def bellman(self, n, flights, src, dst, k, g):
        cost = [float('inf')] * n
        cost[src] = 0
        for i in range(k + 1):
            cur = cost[:]

            for s in g:
                for d in g[s]:
                    if cost[s] != float('inf') and cost[s] + g[s][d] < cur[d]:
                        cur[d] = cost[s] + g[s][d]
            cost = cur[:]

        return cost[dst] if cost[dst] != float('inf') else -1