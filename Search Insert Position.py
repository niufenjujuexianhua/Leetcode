# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:48:51 2017

@author: twu
in solution 3
l = m + 1 instead of l = m
r = m - 1 instead of r = m

"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        
        for idx, value in enumerate(nums):
            if value < target and nums[idx+1] > target:
                return idx + 1
            elif value == target:
                return idx
                
                
class Solution2(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """       
        return len([x for x in nums if x<target])
        
        
class Solution3(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """       
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
            
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        return l
        
if __name__ == '__main__':
    result = Solution3().searchInsert([1,3,5],2)
    print(result)
