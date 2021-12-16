class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        import collections
        g = collections.defaultdict(dict)

        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]
            g[a][b] = v
            g[b][a] = 1.0 / v

        res = []
        for s, e in queries:
            if s in g and e in g[s]:
                res.append(g[s][e])
                continue

            v = self.dfs(g, s, e, 1.0, set())
            if v != -1:
                g[s][e] = v
                g[e][s] = 1.0 / v
            res.append(v)
        return res


    def dfs(self, g, s, e, path, seen):
        if s not in g or e not in g or s in seen:
            return -1

        if s == e:
            return path
        
        seen.add(s)
        for nxt in g[s]:
            # tmp = g[s][nxt]
            val = self.dfs(g, nxt, e, path * g[s][nxt], seen)
            if val != -1:
                return val 
        return -1 