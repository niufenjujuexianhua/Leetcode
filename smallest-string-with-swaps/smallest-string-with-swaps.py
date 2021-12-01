class UnionFind():
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n
        self.cnt = n

    def find(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.cnt -= 1
            if self.r[px] < self.r[py]:
                self.p[px] = self.p[py]
            elif self.r[px] > self.r[py]:
                self.p[py] = self.p[px]
            else:
                self.p[px] = self.p[py]
                self.r[py] += 1
            return True
        else:
            return False

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        import collections
        if not pairs:
            return s

        uf = UnionFind(len(s))
        for i, j in pairs:
            uf.union(i, j)

        dti = collections.defaultdict(list)
        dtv = collections.defaultdict(list)
        for i in range(len(s)):
            dti[uf.find(i)].append(i)
            dtv[uf.find(i)].append(s[i])

        res = [''] * len(s)
        for root in dti:
            vals = sorted(dtv[root])
            idx = sorted(dti[root])
            for val, i in zip(vals, idx):
                res[i] = val
        return ''.join(res)