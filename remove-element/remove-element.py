class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j, n in enumerate(nums):
            if n != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i 
        