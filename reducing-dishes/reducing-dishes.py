class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        import heapq
        hq, nonneg = [], []
        for s in satisfaction:
            if s < 0:
                heapq.heappush(hq, -s)
            else:
                nonneg.append(s)
        res = sum([v * (i + 1) for i, v in enumerate(sorted(nonneg))])
        pos = sum(nonneg)
        neg = 0

        while hq:
            s = -heapq.heappop(hq)
            if s + neg + pos > 0:
                res += s + neg + pos
            else:
                break
            neg += s 
        return res