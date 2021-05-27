class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = neg = 0
        if nums[0] > 0: pos += 1
        if nums[0] < 0: neg += 1
        ans = pos
        for n in nums[1:]:
            if n > 0:
                pos += 1
                neg = 1 + neg if neg > 0 else 0
            elif n < 0:
                npos = 1 + neg if neg > 0 else 0
                neg = 1 + pos
                pos = npos 
            else:
                pos = neg = 0
            ans = max(ans, pos)
        return ans