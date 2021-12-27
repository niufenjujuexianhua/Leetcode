class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        import collections
        g = collections.defaultdict(list)
        n = len(tickets)

        for s, e in tickets:
            g[s].append(e)

        for s in g:
            g[s] = collections.deque(sorted(g[s]))

        res = []
        self.dfs(g, 'JFK', ['JFK'], res, n)
        return res[0]

    def dfs(self, g, s, path, res, n):
        if res:
            return
        if len(path) == n + 1:
            res.append(path)
            return


        sz = len(g[s])
        for _ in range(sz):
            nxt = g[s].popleft()
            self.dfs(g, nxt, path + [nxt], res, n)
            g[s].append(nxt)