# Given an integer array arr, remove a subarray (can be empty) from arr such tha
# t the remaining elements in arr are non-decreasing. 
# 
#  A subarray is a contiguous subsequence of the array. 
# 
#  Return the length of the shortest subarray to remove. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [1,2,3,10,4,2,3,5]
# Output: 3
# Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The 
# remaining elements after that will be [1,2,3,3,5] which are sorted.
# Another correct solution is to remove the subarray [3,10,4]. 
# 
#  Example 2: 
# 
#  
# Input: arr = [5,4,3,2,1]
# Output: 4
# Explanation: Since the array is strictly decreasing, we can only keep a single
#  element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] o
# r [4,3,2,1].
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [1,2,3]
# Output: 0
# Explanation: The array is already non-decreasing. We do not need to remove any
#  elements.
#  
# 
#  Example 4: 
# 
#  
# Input: arr = [1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 10^5 
#  0 <= arr[i] <= 10^9 
#  
#  Related Topics Array Binary Search 
#  👍 511 👎 17


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        res = n - 1

        j = n - 1
        while j - 1 >= 0 and arr[j] >= arr[j - 1]:
            j -= 1
        if j == 0: return 0
        res = min(res, j)

        for i in range(n):
            if i - 1 >= 0 and arr[i] < arr[i - 1]:
                break
            while j < n and arr[i] > arr[j]:
                j += 1
            res = min(res, j - i - 1)
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
