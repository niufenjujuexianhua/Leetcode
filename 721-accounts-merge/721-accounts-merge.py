class UnionFind():
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.p[py] = px
            elif self.rank[px] < self.rank[py]:
                self.p[px] = py
            else:
                self.p[px] = py
                self.rank[py] += 1
        return

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        import collections
        uf = UnionFind(len(accounts))
        e2id = collections.defaultdict(list)

        for i, acc in enumerate(accounts):
            for j in range(1, len(acc)):
                e2id[acc[j]].append(i)

        for em, accs in e2id.items():
            for i in range(1, len(accs)):
                uf.union(accs[0], accs[i])

        dt = collections.defaultdict(set)
        for i in range(len(accounts)):
            dt[uf.find(i)].add(i)

        res = []
        for accs in dt.values():
            accs = list(accs)
            emails = set()
            for i in accs:
                emails |= set(accounts[i][1:])
            res.append([accounts[accs[0]][0]] + sorted(emails))
        return res