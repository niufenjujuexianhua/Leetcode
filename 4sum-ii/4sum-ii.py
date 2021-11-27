class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        dt1 = collections.Counter(nums1)
        dt2 = collections.Counter(nums2)
        dt3 = collections.Counter(nums3)
        dt4 = collections.Counter(nums4)
        
        ss = collections.defaultdict(int)
        for key1 in dt1:
            for key2 in dt2:
                ss[key1 + key2] += dt1[key1] * dt2[key2]
        
        res = 0 
        for key3 in dt3:
            for key4 in dt4:
                res += ss[-key3 - key4] * dt3[key3] * dt4[key4]
        
        return res 