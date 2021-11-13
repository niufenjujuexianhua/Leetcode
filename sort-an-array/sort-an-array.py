class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums 
        
        lt, rt = self.sortArray(nums[: n//2]), self.sortArray(nums[n//2 :])
        
        res = [] 
        i = j = 0 
        while i < len(lt) and j < len(rt):
            if lt[i] <= rt[j]:
                res.append(lt[i])
                i += 1 
            else:
                res.append(rt[j])
                j += 1
        res.extend(lt[i:])
        res.extend(rt[j:])
        return res 