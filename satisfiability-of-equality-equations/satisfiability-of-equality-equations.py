import collections
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        diff = set()

        for e in equations:
            u, v = e[0], e[-1]
            if e[1] == '=':
                graph[u].add(v)
                graph[v].add(u)
            else:
                diff.add((u, v))

        for u, v in diff:
            if self.connect(u, v, graph, set()):
                return False
        return True

    def connect(self, u, v, graph, seen):
        if u == v:
            return True
        if u in seen:
            return False 
        seen.add(u)
        for nxt in graph[u]:
            # if nxt not in seen:
            if self.connect(nxt, v, graph, seen):
                return True
        return False


# print(Solution().equationsPossible(["b==a","a==b"]))
