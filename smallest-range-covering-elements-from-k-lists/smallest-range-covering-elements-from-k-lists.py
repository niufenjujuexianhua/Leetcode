class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)
        right = max(row[0] for row in nums)
        ans = float('-inf'), float('inf')

        while pq:
            left, r, c = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right

            if c + 1 == len(nums[r]):
                return ans

            right = max(right, nums[r][c + 1])
            heapq.heappush(pq, (nums[r][c + 1], r, c + 1))