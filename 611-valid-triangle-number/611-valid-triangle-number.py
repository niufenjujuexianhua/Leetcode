class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        for i in reversed(range(2, len(nums))):
            c = nums[i]
            s, e = 0, i - 1
            while s < e:
                if nums[s] + nums[e] > c:
                    res += e - s
                    e -= 1
                else:
                    s += 1
        return res