class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]

        a +- b * c
        L  O C i
             L O
        """
        res = []
        self.dfs(num, 0, None, '', 0, res, target)
        return res

    def dfs(self, s, i, prev, path, total, res, target):
        if i == len(s):
            if total == target:
                res.append(path)
            return

        for j in range(i + 1, len(s) + 1):
            tmps = s[i : j]
            if tmps[0] == '0' and len(tmps) > 1:
                break
            tmpn = int(tmps)

            if prev is None:
                self.dfs(s, j, tmpn, path + tmps, total + tmpn, res, target)
            else:
                self.dfs(s, j, tmpn, path + '+' + tmps, total + tmpn, res, target)
                self.dfs(s, j, -tmpn, path + '-' + tmps, total - tmpn, res, target)
                self.dfs(s, j, prev * tmpn, path + '*' + tmps, total - prev + prev * tmpn, res, target)