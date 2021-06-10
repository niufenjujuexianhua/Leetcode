class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        if len(nums) == 1:
            return nums[0]

        hq = [(-nums[0], 0)]
        heapq.heapify(hq)
        for i, n in enumerate(nums[1:], 1):
            while hq and hq[0][1] + k < i:
                heapq.heappop(hq)

            if i == len(nums) - 1:
                return n - hq[0][0]

            heapq.heappush(hq, (hq[0][0] - n, i))