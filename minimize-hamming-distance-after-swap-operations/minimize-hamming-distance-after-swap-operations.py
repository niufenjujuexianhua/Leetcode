class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        res = sz = len(source)
        seen = [0] * sz
        g = collections.defaultdict(set)

        for i, j in allowedSwaps:
            g[i].add(j)
            g[j].add(i)

        for i in range(len(source)):
            if not seen[i]:
                found = []
                self.dfs(i, g, found, seen)

                same = collections.Counter([source[i] for i in found]) & collections.Counter([target[i] for i in found])
                res -= sum(same.values())

        return res

    def dfs(self, i, g, found, seen):
        seen[i] = 1
        found.append(i)
        for j in g[i]:
            if not seen[j]:
                self.dfs(j, g, found, seen)