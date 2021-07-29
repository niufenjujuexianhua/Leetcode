class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        hq = []
        res = ss = 0 
        for e, s in sorted([(e, s) for e, s in zip(efficiency, speed)], reverse = 1):
            heapq.heappush(hq, s)
            ss += s 
            
            if len(hq) > k:
                ss -= heapq.heappop(hq)
            
            res = max(res, ss * e)
        return res % (10 ** 9 + 7)