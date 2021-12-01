class unionfind():
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [1] * n
        self.cnt = n

    def find(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.cnt -= 1
            if self.rank[px] < self.rank[py]:
                self.p[px] = self.p[py]
            elif self.rank[px] > self.rank[py]:
                self.p[py] = self.p[px]
            else:
                self.p[px] = self.p[py]
                self.rank[py] += 1


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        uf = unionfind(n)
        
        for i in range(n):
            for j in range(i + 1):
                if isConnected[i][j]:
                    uf.union(i, j)
        return uf.cnt 