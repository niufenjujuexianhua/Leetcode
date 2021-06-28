class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        return self.calc(nums1, nums2) + \
               self.calc(nums2, nums1)


    def calc(self, nums1, nums2):
        import collections
        res = 0
        # sqs = collections.Counter([n * n for n in nums1])
        nums = collections.Counter(nums2)
        for a in nums1:
            sq = a * a
            for n, cntn in nums.items():
                div, mod = divmod(sq, n)
                if mod == 0 and div in nums:
                    if div == n:
                        res += cntn * (cntn - 1)
                    else:
                        res += cntn * nums[div]
            # res //= 2
        return res // 2