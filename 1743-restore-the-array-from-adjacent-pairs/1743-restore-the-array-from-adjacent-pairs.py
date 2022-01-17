class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        import collections
        g = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        for a, b in adjacentPairs:
            g[a].add(b)
            g[b].add(a)
            indegree[a] += 1
            indegree[b] += 1

        for n, ind in indegree.items():
            if ind == 1:
                s = n
                break

        path = []
        self.dfs(g, s, path, set())
        return path
    
    def dfs(self, g, s, path, seen):
        if s in seen:
            return

        path.append(s)
        seen.add(s)

        for nxt in g[s]:
            self.dfs(g, nxt, path, seen)