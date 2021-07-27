class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sz = len(nums)
        nums.sort()
        res = [None, float('inf')]
        
        for k in range(sz - 2):
            ntarget = target - nums[k]
            i, j = k + 1, sz - 1
            
            while i < j:
                ss = nums[i] + nums[j]
                
                if abs(ss - ntarget) < res[1]:
                    res = [ss + nums[k], abs(ss - ntarget)]
                
                if ss == ntarget:
                    return target
                elif ss < ntarget:
                    i += 1 
                else:
                    j -= 1 
        
        return res[0]