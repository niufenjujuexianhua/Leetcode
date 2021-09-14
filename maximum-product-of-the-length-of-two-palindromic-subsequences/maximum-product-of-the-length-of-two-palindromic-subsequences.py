class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cands = []
        for mask in range(1, 1 << n):
            subs = ''
            for i in range(n):
                if mask & (1 << i) > 0:
                    subs += s[i]
            if subs == subs[::-1]:
                cands.append((mask, len(subs)))

        res = 0
        for i in range(len(cands) - 1):
            for j in range(i + 1, len(cands)):
                mask1, sz1 = cands[i]
                mask2, sz2 = cands[j]
                if mask1 & mask2 == 0:
                    res = max(res, sz1 * sz2)
        return res