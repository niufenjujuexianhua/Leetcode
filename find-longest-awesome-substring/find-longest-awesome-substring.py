class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        dt, nodd, i, res = {0:-1}, 0, 0, 1
        st = 0
        for j in range(len(s)):
            n = s[j]
            st ^= (1 << int(n))
            if st in dt:
                res = max(res, j - dt[st])

            for i in range(10):
                nst = st ^ (1 << i)
                if nst in dt:
                    res = max(res, j - dt[nst])
            if st not in dt:
                dt[st] = j 
        return res