class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        tdt = collections.Counter(t)
        pos = len(tdt)
        i = 0
        res = [float('-inf'), float('inf')]
        for j, ch in enumerate(s):
            if ch in tdt:
                tdt[ch] -= 1
                if tdt[ch] == 0:
                    pos -= 1

            while pos == 0:
                if j - i < res[1] - res[0]:
                    res = [i, j]
                tmpch = s[i]
                if tmpch in tdt:
                    tdt[tmpch] += 1
                    if tdt[tmpch] == 1:
                        pos += 1
                i += 1
        i, j = res[0], res[1]
        return s[i : j + 1] if i != float('-inf') else ''