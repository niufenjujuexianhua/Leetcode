class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = collections.defaultdict(dict)

        for i, (a, b) in enumerate(equations):
            g[a][b] = values[i]
            g[b][a] = 1.0 / values[i]

        res = []
        for s, d in queries:
            v = self.dfs(g, s, d, 1.0, set())
            if v != -1:
                g[s][d] = v
                g[d][s] = 1.0 / v
            res.append(v)
        return res

    def dfs(self, g, s, d, path, seen):
        if s not in g or d not in g or s in seen:
            return -1.0
        if s == d:
            return path

        seen.add(s)
        for nxt in g[s]:
            tmp = self.dfs(g, nxt, d, path * g[s][nxt], seen)
            if tmp != -1.0:
                return tmp
        return -1.0