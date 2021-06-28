class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if len(nums1) * 6 < len(nums2) or len(nums1) > len(nums2) * 6:
            return -1
        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2:
            nums1, nums2 = nums2, nums1
        diff = abs(s1 - s2)
        if diff == 0:
            return 0 
        cnt = [0] * 6
        for n in nums1:
            cnt[6 - n] += 1
        for n in nums2:
            cnt[n - 1] += 1

        res, i = 0, 5
        while diff > 0:
            while cnt[i] == 0:
                i -= 1
                if i < 0:
                    break
            diff -= i
            cnt[i] -= 1
            res += 1
            if diff <= 0:
                return res 

        return -1