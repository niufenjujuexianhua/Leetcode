class UnionFind():
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [1] * n
        self.cnt = n

    def find(self, x):
        if x != self.p[x]:
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
                self.p[py] = self.p[px]
                self.r[px] += 1

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        import collections
        emailid = {}
        e2p = {}
        id = 0
        for acc in accounts:
            for em in acc[1:]:
                if em not in emailid:
                    emailid[em] = id
                    id += 1
                e2p[emailid[em]] = acc[0]

        uf = UnionFind(len(emailid))
        for acc in accounts:
            for em in acc[2:]:
                uf.union(emailid[acc[1]], emailid[em])

        roots = collections.defaultdict(list)
        for em, id in emailid.items():
            roots[uf.find(id)].append(em)

        res = []
        for id, ems in roots.items():
            res.append([e2p[id]] + sorted(ems))
        return res 