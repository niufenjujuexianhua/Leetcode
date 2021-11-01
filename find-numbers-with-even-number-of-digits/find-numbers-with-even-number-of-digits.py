class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [0, 10)
        [10, 100)
        [100, 1000)
        [1000, 10000)
        [10000, 100000)
        
        
        """
        res = 0
        for n in nums:
            if 10 <= n < 100 or 1000 <= n < 10000 or n == 100000:
                res += 1 
        return res 