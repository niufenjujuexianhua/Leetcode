class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        hq = []
        res = 0
        i = 0
        for day in range(1, 100001):
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(hq, events[i][1])
                i += 1

            while hq and hq[0] < day:
                heapq.heappop(hq)

            if hq:
                heapq.heappop(hq)
                res += 1
        return res