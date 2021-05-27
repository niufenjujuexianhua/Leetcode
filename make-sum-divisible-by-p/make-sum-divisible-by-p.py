class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums)
        if total % p == 0:
            return 0
        if total < p:
            return -1
        need = total % p


        dt, cur, res = {0 : -1}, 0, len(nums)
        for i, n in enumerate(nums):
            cur = (cur + n) % p
            dt[cur] = i 
            if (cur - need) % p in dt:
                res = min(res, i - dt[(cur - need) % p])

        return res if res != len(nums) else -1 