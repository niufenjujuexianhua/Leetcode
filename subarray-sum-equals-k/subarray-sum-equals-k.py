class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dt = collections.defaultdict(int)
        dt[0] = 1
        ss, res = 0, 0
        for n in nums:
            ss += n
            res += dt[ss - k]
            dt[ss] += 1
        return res