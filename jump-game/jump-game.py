class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mn = nums[0]
        for i in range(1, len(nums)):
            if mn < i:
                return False
            if mn >= len(nums) - 1:
                return True
            mn = max(mn, i + nums[i])

        return True