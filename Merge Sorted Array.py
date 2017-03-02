class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        indexM, indexN = m - 1, n - 1

        while indexM > -1 and indexN > -1:
            index = indexM + indexN + 1
            if nums1[indexM] > nums2[indexN]:
                nums1[index] = nums1[indexM]
                indexM -= 1
            else:
                nums1[index] = nums2[indexN]
                indexN -= 1

        if indexN > -1:
            nums1[:indexN + 1] = nums2[:indexN + 1]


if __name__ == '__main__':
    result = Solution().merge([1],1,[2,3,4],3)
    print(result)