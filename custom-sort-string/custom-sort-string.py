class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        import collections
        res = ''
        sdt = collections.Counter(s)
        for ch in order:
            if ch in sdt:
                res += ch * sdt[ch]
                del sdt[ch]

        for ch in sdt:
            res += ch * sdt[ch]
            # del sdt[ch]

        return res