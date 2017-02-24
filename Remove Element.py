# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:43:59 2017

@author: twu
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end-1
            else:
                start += 1
        return start
            
class Solution2(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = [x for x in nums if x != val]
        return len(nums)
        
        

        
if __name__ == '__main__':
    result = Solution2().removeElement([3,2,2,3], 3)
    print(result)