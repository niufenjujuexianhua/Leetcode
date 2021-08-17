class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0 
        for i in range(0, len(nums) + 1):
            res ^= i 
        for n in nums:
            res ^= n 
        return res 