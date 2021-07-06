class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sz = len(nums)
        lt, rt = [nums[0]], [nums[-1]] 
        
        for i in range(1, sz):
            lt.append(nums[i] * lt[-1])
        
        for i in reversed(range(sz - 1)):
            rt.append(nums[i] * rt[-1])
        rt.reverse()
        
        res = [] 
        for i in range(sz):
            if i == 0:
                res.append(rt[i + 1])
            elif i == sz - 1:
                res.append(lt[i - 1])
            else:
                res.append(lt[i - 1] * rt[i + 1])
        return res 