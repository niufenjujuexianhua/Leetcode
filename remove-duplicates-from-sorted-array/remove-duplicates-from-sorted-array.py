class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1, len(nums)):
            n = nums[j]
            if n == nums[i]:
                continue
            i += 1
            nums[i] = n
        return i + 1