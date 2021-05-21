class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        lt, res, i, n = 0, 0, 0, len(s)
        while i < n:
            c = s[i]
            if c == '(':
                lt += 1
                i += 1
            else:
                if i < n - 1 and s[i+1] == ')':
                    if lt:
                        lt -= 1
                    else:
                        res += 1
                    i += 2
                else:
                    if lt:
                        lt -= 1
                        res += 1
                    else:
                        res += 2
                    i += 1
        res += lt * 2
        return res
        