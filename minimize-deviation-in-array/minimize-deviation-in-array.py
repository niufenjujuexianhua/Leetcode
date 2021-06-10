class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hq = [-n if n % 2 == 0 else -n * 2 for n in nums]
        heapq.heapify(hq)
        mi, res = -max(hq), float('inf')
        while len(hq) == len(nums):
            n = -heapq.heappop(hq)
            res = min(res, n - mi)
            
            if n % 2 == 0:
                mi = min(mi, n // 2)
                heapq.heappush(hq, -n // 2)
        return res 