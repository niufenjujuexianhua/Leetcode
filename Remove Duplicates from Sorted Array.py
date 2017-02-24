# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:58:12 2017

@author: twu
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return len(nums)
            
        pos = 0
        for i in range(1, len(nums)):
            if nums[pos] != nums[i]:
                pos +=  1
                nums[pos] = nums[i]

        return pos+1
            

#        length = len(nums)
#        
#        for idx in range(length-1):
#            if nums[idx] == nums[idx+1]:
#                del nums[idx]
#                length -= 1
#        
#        if nums[-2] == nums[-1]:
#            del nums[-1]
#
#        return nums
        
if __name__ == '__main__':
    result = Solution().removeDuplicates([1])
    print(result)