# Given two integer arrays arr1 and arr2, return the minimum number of operation
# s (possibly zero) needed to make arr1 strictly increasing. 
# 
#  In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j 
# < arr2.length and do the assignment arr1[i] = arr2[j]. 
# 
#  If there is no way to make arr1 strictly increasing, return -1. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# Output: 1
# Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
#  
# 
#  Example 2: 
# 
#  
# Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# Output: 2
# Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7
# ].
#  
# 
#  Example 3: 
# 
#  
# Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# Output: -1
# Explanation: You can't make arr1 strictly increasing. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr1.length, arr2.length <= 2000 
#  0 <= arr1[i], arr2[i] <= 10^9 
#  
# 
#  Related Topics Dynamic Programming 
#  👍 331 👎 8


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache
from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        ls = sorted(set(arr2))

        @lru_cache(None)
        def dfs(i, cur_min):
            if i >= len(arr1):
                return 0

            j = bisect_right(ls, cur_min)
            swap = 1 + dfs(i + 1, ls[j]) if j < len(ls) else float("inf")
            noswap = dfs(i + 1, arr1[i]) if arr1[i] > cur_min else float("inf")

            return min(swap, noswap)

        changes = dfs(0, float("-inf"))
        return changes if changes != float("inf") else -1
        
# leetcode submit region end(Prohibit modification and deletion)
