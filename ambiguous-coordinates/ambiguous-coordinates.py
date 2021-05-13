class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        0001   1
        1. len(s) > 1 and all 0    000
        2. first and last are 0    010

        1. starts with 0   0.123
        2. ends with 0     120
        else:              1.23  12.3
        """
        s = s[1:-1]
        n, res = len(s), []
        for i in range(1, n):
            lt, rt = s[:i], s[i:]
            if self.invalid(lt) or self.invalid(rt):
                continue

            ltres, rtres = self.addDec(lt), self.addDec(rt)
            res.extend(['(' + l + ', ' + r + ')' for l in ltres for r in rtres])
        return res

    def invalid(self, s):
        if len(s) >= 2 and s[0] == s[-1] == '0':
            return True
        return False

    def addDec(self, s):
        res = []
        if len(s) == 1:
            res.append(s)
        elif s[0] == '0':
            res.append(s[:1] + '.' + s[1:])
        elif s[-1] == '0':
            res.append(s)
        else:
            for i in range(1, len(s)):
                res.append(s[:i] + '.' + s[i:])
            res.append(s)
        return res