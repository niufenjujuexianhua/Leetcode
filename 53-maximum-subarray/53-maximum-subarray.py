class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        running = nums[0]
        for n in nums[1:]:
            if running <= 0:
                running = n
            else:
                running += n 
            res = max(res, running)
        return res