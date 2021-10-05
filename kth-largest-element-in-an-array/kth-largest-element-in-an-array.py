class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        1 2 3 4
        [3 4]
        """
        import heapq
        hq = []
        for n in nums:
            if len(hq) < k:
                heapq.heappush(hq, n)
            elif n > hq[0]:
                heapq.heappushpop(hq, n)

        return hq[0]