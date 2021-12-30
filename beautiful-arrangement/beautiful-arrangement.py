class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        seen = [0] * (n + 1)
        res = [0]
        self.dfs(n, seen, [], res)
        return res[0]

    def dfs(self, n, seen, path, res):
        if len(path) == n:
            res[0] += 1
            return

        for i in range(1, n + 1):
            if not seen[i]:
                if i % (len(path) + 1) == 0 or (len(path) + 1) % i == 0:
                    seen[i] = 1
                    self.dfs(n, seen, path + [i], res)
                    seen[i] = 0
