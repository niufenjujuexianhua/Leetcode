class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        lt, rt, valid = self.valid(s)
        if valid: return [s]
        res = set()
        self.dfs(s, lt, rt, set(), res)
        return res

    def dfs(self, s, lt, rt, seen, res):
        if (s, lt, rt) in seen:
            return
        if lt == rt == 0:
            _, _, valid = self.valid(s)
            if valid:
                res.add(s)
            return

        seen.add((s, lt, rt))
        for i, ch in enumerate(s):
            if ch == '(' and lt > 0:
                self.dfs(s[:i] + s[i + 1:], lt - 1, rt, seen, res)
            elif ch == ')' and rt > 0:
                self.dfs(s[:i] + s[i + 1:], lt, rt - 1, seen, res)

    def valid(self, s):
        lt = rt = 0
        for ch in s:
            if ch == '(':
                lt += 1
            elif ch == ')':
                if lt > 0:
                    lt -= 1
                else:
                    rt += 1
        return lt, rt, lt == rt == 0