class UnionFind():
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [1] * n

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return True

        if self.r[px] < self.r[py]:
            self.p[px] = self.p[py]
        elif self.r[px] > self.r[py]:
            self.p[py] = self.p[px]
        else:
            self.p[py] = self.p[px]
            self.r[px] += 1
        return False

class Solution(object):
    def makeConnected(self, n, edges):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(edges) < n - 1:
            return -1 
        uf = UnionFind(n)
        redundant = []
        for s, e in edges:
            if uf.union(s, e):
                redundant.append([s, e])

        isolated = set([uf.find(i) for i in range(n)])
        return len(isolated) - 1