class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        pc = sorted([(p, c) for p, c in zip(profits, capital)], key = lambda x : -x[1])

        pros = []
        while k:
            while pc and pc[-1][1] <= w:
                heapq.heappush(pros, -pc.pop()[0])

            if pros:
                w -= heapq.heappop(pros)
            else:
                break
            k -= 1

        return w