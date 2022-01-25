class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        self.dfs(num, 0, '', 0, None, target, res)
        return res


    def dfs(self, num, i, path, total, prev, target, res):
        if i == len(num):
            if total == target:
                res.append(path)
            return

        for j in range(i, len(num)):
            if num[i] == '0' and j > i:
                break
            tmps = num[i:j + 1]
            tmpn = int(tmps)
            if prev is None:
                self.dfs(num, j + 1, path + tmps, total + tmpn, tmpn, target, res)
            else:
                self.dfs(num, j + 1, path + '+' + tmps, total + tmpn, tmpn, target, res)
                self.dfs(num, j + 1, path + '-' + tmps, total - tmpn, -tmpn, target, res)
                self.dfs(num, j + 1, path + '*' + tmps, total - prev + prev * tmpn, prev * tmpn, target, res)
