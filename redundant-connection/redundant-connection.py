class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        import collections
        g = collections.defaultdict(set)
        for s, e in edges:
            if s in g and e in g and self.cycle(g, s, e, set()):
                return [s, e]
            g[s].add(e)
            g[e].add(s)
        return []


    def cycle(self, g, s, e, seen):
        if s == e:
            return True
        if s in seen:
            return False

        seen.add(s)
        for nxt in g[s]:
            if self.cycle(g, nxt, e, seen):
                return True
        return False