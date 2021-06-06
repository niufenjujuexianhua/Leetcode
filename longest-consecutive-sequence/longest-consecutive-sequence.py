class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums, res = set(nums), 0
        while nums:
            n = nums.pop()
            lt = rt = n 
            while rt + 1 in nums:
                nums.remove(rt + 1)
                rt += 1 
            while lt - 1 in nums:
                nums.remove(lt - 1)
                lt -= 1
            res = max(res, rt - lt + 1)
        return res