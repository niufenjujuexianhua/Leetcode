class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        import collections
        dt = collections.defaultdict(set)

        for i, acc in enumerate(accounts):
            for em in acc[1:]:
                dt[em].add(i)

        res = []
        seen = set()
        for i in range(len(accounts)):
            if i not in seen:
                emails = set()
                self.dfs(accounts, i, seen, dt, emails)

                res.append([accounts[i][0]] + sorted(emails))
        return res

    def dfs(self, accounts, i, seen, dt, emails):
        if i in seen:
            return
        seen.add(i)
        for em in accounts[i][1:]:
            emails.add(em)
            for j in dt[em]:
                self.dfs(accounts, j, seen, dt, emails)