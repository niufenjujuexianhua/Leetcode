class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lt = rt = res = 0
        for c in s:
            lt += c == '('
            rt += c == ')'

            if lt == rt:
                res = max(res, lt + rt)
            if rt > lt:
                lt = rt = 0

        lt = rt = 0
        for c in s[::-1]:
            lt += c == '('
            rt += c == ')'

            if lt == rt:
                res = max(res, lt + rt)
            if rt < lt:
                lt = rt = 0
        return res