class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            if nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] *= -1
        
        res = [] 
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res 