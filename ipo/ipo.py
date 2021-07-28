class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        import heapq
        if w < min(capital):
            return w

        proj = sorted([(c, p) for c, p in zip(capital, profits)])
        i = 0
        hq = []

        for _ in range(k):
            while i < len(proj) and proj[i][0] <= w:
                heapq.heappush(hq, -proj[i][1])
                i += 1
            
            if hq:
                w -= heapq.heappop(hq)
            
            # if i < len(proj) and w < proj[i][0] or not hq:
            #     break

        return w