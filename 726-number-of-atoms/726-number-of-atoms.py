class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        self.i = 0
        dt = self.dfs(list(formula))
        res = ''
        for k, v in sorted(dt.items()):
            if v > 1:
                res += k + str(v)
            else:
                res += k
        return res

    def dfs(self, formula):
        import collections
        dt = collections.defaultdict(int)
        while self.i < len(formula):
            if formula[self.i] == '(':
                self.i += 1
                tmp_dt = self.dfs(formula)
                cnt = self.getCount(formula)

                for name in tmp_dt:
                    dt[name] = dt[name] + tmp_dt[name] * cnt

            elif formula[self.i] == ')':
                self.i += 1
                return dt
            else:
                name = self.getName(formula)
                cnt = self.getCount(formula)

                dt[name] = dt[name] + cnt

        return dt
            


    def getName(self, formula):
        name = formula[self.i]
        self.i += 1
        while self.i < len(formula) and formula[self.i].islower():
            name += formula[self.i]
            self.i += 1
        return name


    def getCount(self, formula):
        cnt = ''
        while self.i < len(formula) and formula[self.i].isdigit():
            cnt += formula[self.i]
            self.i += 1
        return int(cnt) if cnt != '' else 1