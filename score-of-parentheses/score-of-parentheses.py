class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.dfs(s, 0, len(s) - 1)

    def dfs(self, s, b, e):
        if b + 1 == e:
            return 1

        i, cnt = b, 0
        for i in range(b, e + 1):
            if s[i] == '(':
                cnt += 1
            else:
                cnt -= 1

            if cnt == 0:
                break

        if i == e:
            return 2 * self.dfs(s, b + 1, e - 1)
        else:
            return self.dfs(s, b, i) + \
                   self.dfs(s, i + 1, e)