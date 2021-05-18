class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {}
        return self.dfs(s, 0, 0, m)

    def dfs(self, s, lt, i, m):
        if lt < 0:
            return False
        if i == len(s):
            return lt == 0
        if (i, lt) in m:
            return m[(i, lt)]

        ans = False
        if s[i] == '*':
            ans = (self.dfs(s, lt + 1, i + 1, m) or
                    self.dfs(s, lt - 1, i + 1, m) or
                    self.dfs(s, lt    , i + 1, m))
        else:
            ans = self.dfs(s, lt + [1, -1][s[i] == ')'], i + 1, m)
        m[(i, lt)] = ans
        return ans