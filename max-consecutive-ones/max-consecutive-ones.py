class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = cnt = 0 
        for n in nums:
            if n == 1:
                cnt += 1 
                res = max(res, cnt)
            else:
                cnt = 0 
        return res 