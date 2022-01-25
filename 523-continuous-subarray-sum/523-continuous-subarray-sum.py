class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        import collections
        dt = {0:-1}
        res = 0
        total = 0
        for i, n in enumerate(nums):
            total = (total + n) % k
            if total in dt:
                if i - dt[total] >= 2:
                    return True
            else:
                dt[total] = i 
        return False