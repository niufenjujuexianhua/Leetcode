class Solution(object):
    def maxSum(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i, j, m, n = 0, 0, len(A), len(B)
        a = b = 0
        while i < m or j < n:
            if i < m and (j == n or A[i] < B[j]):
                a += A[i]
                i += 1
            elif j < n and (i == m or B[j] < A[i]):
                b += B[j]
                j += 1
            else:
                a = b = max(a, b) + A[i]
                i += 1
                j += 1

        return max(a, b) % (10**9 + 7)