class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        res = []
        seen = set()
        hq = [(nums1[0] + nums2[0], 0, 0)]
        m, n = len(nums1), len(nums2)
        while hq and len(res) < k:
            s, i, j = heapq.heappop(hq)
            res.append((nums1[i], nums2[j]))

            if i + 1 < m and (i + 1, j) not in seen:
                seen.add((i + 1, j))
                heapq.heappush(hq, (nums1[i + 1] + nums2[j], i + 1, j))
            if j + 1 < n and (i, j + 1) not in seen:
                seen.add((i, j + 1))
                heapq.heappush(hq, (nums1[i] + nums2[j + 1], i, j + 1))
        return res