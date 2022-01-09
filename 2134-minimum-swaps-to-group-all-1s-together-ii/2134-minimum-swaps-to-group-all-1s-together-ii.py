class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = sum(nums)
        # sz = len(nums)
        s = 0
        zeros = 0
        res = float('inf')
        for e in range(len(nums) + ones - 1):
            end = e % len(nums)
            zeros += nums[end] == 0

            if end >= s and end - s + 1 == ones + 1 or end <= s and end + 1 + len(nums) - s == ones + 1:
                zeros -= nums[s] == 0
                s += 1

            if end >= s and end - s + 1 == ones or end <= s and end + 1 + len(nums) - s == ones:
                res = min(res, zeros)

        return res if res != float('inf') else 0