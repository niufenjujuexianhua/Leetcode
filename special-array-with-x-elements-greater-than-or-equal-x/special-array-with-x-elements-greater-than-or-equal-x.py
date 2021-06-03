class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, e = 0, len(nums)
        while s + 1 < e:
            m = s + (e - s) // 2
            if self.check(nums, m) == m:
                return m
            elif self.check(nums, m) > m:
                s = m
            else:
                e = m
        if self.check(nums, s) == s:
            return s
        if self.check(nums, e) == e:
            return e
        return -1

    def check(self, nums, m):
        return sum([1 for n in nums if n >= m])