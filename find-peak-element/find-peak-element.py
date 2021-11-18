class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, e = 0, len(nums) - 1

        while s <= e:
            if s == e:
                return s 
            if s + 1 == e:
                return s if nums[s] > nums[e] else e
            
            m = s + (e - s) // 2
            if nums[m - 1] <= nums[m] and nums[m] >= nums[m + 1]:
                return m 
            elif nums[m] <= nums[m + 1]:
                s = m + 1
            else:
                e = m - 1
        return -1