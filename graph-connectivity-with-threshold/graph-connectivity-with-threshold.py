class UnionFind(object):
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py
                self.rank[py] += self.rank[px]
                self.rank[px] = 0
            else:
                self.p[py] = px
                self.rank[px] += self.rank[py]
                self.rank[py] = 0

class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        uf = UnionFind(n + 1)

        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                if i > threshold:
                    uf.union(j, i)

        return [uf.find(a) == uf.find(b) for a, b in queries]