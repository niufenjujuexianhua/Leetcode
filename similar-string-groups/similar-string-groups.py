class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        import collections
        g = collections.defaultdict(set)

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                cnt = sum(int(a != b) for a, b in zip(strs[i], strs[j]))
                if cnt <= 2:
                    g[i].add(j)
                    g[j].add(i)



        seen = [0] * len(strs)
        res = 0
        for i in range(len(strs)):
            if seen[i] == 0:
                self.dfs(g, i, seen)
                res += 1
        return res


    def dfs(self, g, i, seen):
        if seen[i] == 1:
            return

        seen[i] = 1
        for nxt in g[i]:
            self.dfs(g, nxt, seen)