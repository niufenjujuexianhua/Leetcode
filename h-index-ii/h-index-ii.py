class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        s, e = 0, n - 1
        while s + 1 < e:
            m = s + (e - s) // 2
            if citations[m] >= n - m:
                e = m
            else:
                s = m

        if n - s <= citations[s]:
            return n - s
        if n - e <= citations[e]:
            return n - e
        return 0 