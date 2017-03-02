class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        import collections
        d1 = collections.Counter(nums1)
        d2 = collections.Counter(nums2)

        ls = [[k]*min(d1[k], d2[k]) for k in set(d1.keys()) & set(d2.keys())]
        return [j for i in ls for j in i]



class Solution2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in set(nums1):
            if i in nums2:
                n = min(nums1.count(i), nums2.count(i))
                res = res + [i for k in range(n)]
        return res

class Solution3(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        res = []
        while nums1 and nums2:
            if nums1[0] == nums2[0]:
                res.append(nums2.pop(0))
                nums1.pop(0)
            else:
                if nums1[0] < nums2[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)
        return res
class Solution4(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        import collections
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        return list((counter1 & counter2).elements())



if __name__ == '__main__':
    result = Solution3().intersect([-2147483648,1,1,2,3],[1,1,-2147483648,-2147483648])
    print(result)