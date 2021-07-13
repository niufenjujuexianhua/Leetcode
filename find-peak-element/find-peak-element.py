class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s, e = 0, n - 1

        while s + 1 < e:
            m = s + (e - s) // 2
            if nums[m] > nums[m + 1]:
                e = m
            else:
                s = m

        if nums[s] > nums[e]:
            return s
        return e