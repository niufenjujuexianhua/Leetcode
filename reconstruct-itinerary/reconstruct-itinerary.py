class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        import collections
        g = collections.defaultdict(list)
        for s, e in tickets:
            g[s].append(e)

        for s in g:
            g[s] = collections.deque(sorted(g[s], reverse = True))

        res = []
        self.dfs(g, 'JFK', ['JFK'], res, len(tickets) + 1)
        return res[0]

    def dfs(self, g, s, path, res, n):
        if len(path) == n:
            res.append(path)
            return True
        if s not in g or not g[s]:
            return False
        
        sz = len(g[s])
        for _ in range(sz):
            nxt = g[s].pop()
            if self.dfs(g, nxt, path + [nxt], res, n):
                return True
            g[s].appendleft(nxt)
        return False

# print(Solution().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
