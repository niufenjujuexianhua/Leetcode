class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def valid(m):
            cnt = lt = 0 
            for rt, n in enumerate(nums):
                while nums[rt] - nums[lt] > m:
                    lt += 1 
                cnt += rt - lt 
            return cnt >= k

        nums.sort()
        s, e = 0, nums[-1] - nums[0]
        while s + 1 < e:
            m = s + (e - s) // 2
            if valid(m):
                e = m
            else:
                s = m
        if valid(s):
            return s 
        if valid(e):
            return e 