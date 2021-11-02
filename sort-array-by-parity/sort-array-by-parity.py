class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = -1
        for j, n in enumerate(nums):
            if n % 2 == 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return nums