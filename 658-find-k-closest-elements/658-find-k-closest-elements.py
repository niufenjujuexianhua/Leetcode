class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        import collections
        if len(arr) == k:
            return arr

        i, j = 0, len(arr) - 1
        while j - i + 1 > k:
            if abs(arr[j] - x) >= abs(arr[i] - x):
                j -= 1
            else:
                i += 1
        return arr[i : j + 1]