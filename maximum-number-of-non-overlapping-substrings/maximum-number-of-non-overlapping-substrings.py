class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dt, sset = {}, set(s)
        for i, ch in enumerate(s):
            if ch not in dt:
                dt[ch] = [float('inf'), float('-inf')]
            dt[ch][0] = min(dt[ch][0], i)
            dt[ch][1] = max(dt[ch][1], i)

        inter = []
        for ch in sset:
            l, r = dt[ch]
            i = l
            while i <= r and l == dt[ch][0]:
                l = min(l, dt[s[i]][0])
                r = max(r, dt[s[i]][1])
                i += 1
                
            if l == dt[ch][0]:
                inter.append([l, r])
        inter.sort(key = lambda x : x[1])

        res, prev = [], -1
        for l, r in inter:
            if l > prev:
                res.append(s[l : r + 1])
                prev = r
        return res