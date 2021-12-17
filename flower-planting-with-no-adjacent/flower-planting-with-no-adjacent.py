class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        import collections
        g = collections.defaultdict(set)

        for a, b in paths:
            g[a].add(b)
            g[b].add(a)

        res = [0] + [0] * n
        for i in range(1, n + 1):
            possible = set(range(1, 5))
            for nxt in g[i]:
                possible.discard(res[nxt])
            res[i] = possible.pop()
        return res[1:]