class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        for i in reversed(range(len(arr))):
            if i + zeros < len(arr):
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1 
                if i + zeros < len(arr):
                    arr[i + zeros] = arr[i]