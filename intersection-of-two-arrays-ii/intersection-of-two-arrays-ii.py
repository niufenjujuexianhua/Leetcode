class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dt = collections.Counter(nums1)

        res = []
        for n in nums2:
            if n in dt:
                res.append(n)
                dt[n] -= 1 
                if dt[n] == 0:
                    del dt[n]
        return res