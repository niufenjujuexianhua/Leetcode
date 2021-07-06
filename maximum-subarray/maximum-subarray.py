class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sz, res = len(nums), nums[0]

        for i in range(1, sz):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            res = max(res, nums[i])
        return res 