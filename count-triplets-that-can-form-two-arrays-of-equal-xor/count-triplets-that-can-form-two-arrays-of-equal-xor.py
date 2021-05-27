class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr = [0] + arr
        n = len(arr)
        res = 0
        for i in range(1, n):
            arr[i] ^= arr[i - 1]
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    res += j - i - 1
        return res