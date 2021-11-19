class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[-1] > nums[0]:
            return nums[0]
        s, e = 0, len(nums) - 1
        while s + 1 < e:
            m = s + (e - s) // 2
            
            if nums[m] > nums[e]:
                s = m
            elif nums[m] < nums[e]:
                e = m
            else:
                e -= 1
                
        return min(nums[s], nums[e])