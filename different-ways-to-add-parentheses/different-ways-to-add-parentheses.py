class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        ls = []
        n = 0
        for i, e in enumerate(expression):
            if e.isdigit():
                n = n * 10 + int(e)
            else:
                ls.extend([n, e])
                n = 0
        ls.append(n)

        return self.dfs(ls)

    def dfs(self, ls):
        if len(ls) == 1:
            return ls
        if len(ls) == 3:
            return [self.calc(ls[0], ls[2], ls[1])]

        res = []
        for i in range(len(ls)):
            if str(ls[i]) in '+-*':
                lt = self.dfs(ls[:i])
                rt = self.dfs(ls[i + 1:])
                res.extend([self.calc(a, b, ls[i]) for a in lt for b in rt])
        return res


    def calc(self, a, b, op):
        if op == '-':
            return a - b
        if op == '+':
            return a + b
        return a * b