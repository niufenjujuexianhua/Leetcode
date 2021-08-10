class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        size = m + n
        odd = size % 2
        leftside = (size + 1) // 2
        s, e = 0, m

        while s <= e:
            ult = s + (e - s) // 2
            urt = m - ult
            llt = leftside - ult
            lrt = n - llt

            ultmax = nums1[ult - 1] if ult > 0 else float('-inf')
            lltmax = nums2[llt - 1] if llt > 0 else float('-inf')
            urtmin = nums1[ult] if ult < m else float('inf')
            lrtmin = nums2[llt] if llt < n else float('inf')

            if ultmax <= lrtmin and lltmax <= urtmin:
                if odd:
                    return max(ultmax, lltmax)
                else:
                    return (max(ultmax, lltmax) + min(urtmin, lrtmin)) / 2.0
            elif ultmax > lrtmin:
                e = ult - 1
            else:
                s = ult + 1
        