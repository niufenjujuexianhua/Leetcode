class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        seen = [0] * n
        res = [0]
        self.dfs(seen, 0, res)
        return res[0]

    def dfs(self, seen, j, res):
        if j == len(seen):
            res[0] += 1
            return

        for k in range(len(seen)):
            if not seen[k]:
                if (k + 1) % (j + 1) == 0 or (j + 1) % (k + 1) == 0:
                    seen[k] = 1
                    self.dfs(seen, j + 1, res)
                    seen[k] = 0