class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        import collections
        # uf = UnionFind()
        e2id = collections.defaultdict(set)

        for i, acc in enumerate(accounts):
            for j in range(1, len(acc)):
                e2id[acc[j]].add(i)

        seen = [0] * len(accounts)
        res = []
        for i in range(len(accounts)):
            if not seen[i]:
                emails = set()
                self.dfs(accounts, e2id, emails, i, seen)
                # tmp = ' '.join(list(sorted(emails)))
                res.append([accounts[i][0]] + sorted(emails))
                # print(res)
        return res

    def dfs(self, accounts, e2id, emails, i, seen):
        if seen[i]:
            return
        seen[i] = 1
        for em in accounts[i][1:]:
            emails.add(em)
            for j in e2id[em]:
                self.dfs(accounts, e2id, emails, j, seen)