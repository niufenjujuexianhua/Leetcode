class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = -1
        for j, n in enumerate(nums):
            if n != val:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return i + 1 