class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or max(nums) == min(nums): return 0
        mini, maxi = min(nums), max(nums)
        size = (maxi - mini) // (len(nums) - 1) or 1
        bucket = [[float('inf'), float('-inf')] for _ in range((maxi - mini) // size + 1)]

        for n in nums:
            b = bucket[(n - mini) // size]
            b[0] = min(b[0], n)
            b[1] = max(b[1], n)

        bucket = [x for x in bucket if x[0] < float('inf')]
        return max(b[0] - a[1] for a, b in zip(bucket, bucket[1:]))