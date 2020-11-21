# Given two arrays nums1 and nums2. 
# 
#  Return the maximum dot product between non-empty subsequences of nums1 and nu
# ms2 with the same length. 
# 
#  A subsequence of a array is a new array which is formed from the original arr
# ay by deleting some (can be none) of the characters without disturbing the relat
# ive positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2
# ,3,4,5] while [1,5,3] is not). 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# Output: 18
# Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nu
# ms2.
# Their dot product is (2*3 + (-2)*(-6)) = 18. 
# 
#  Example 2: 
# 
#  
# Input: nums1 = [3,-2], nums2 = [2,-6,7]
# Output: 21
# Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
# Their dot product is (3*7) = 21. 
# 
#  Example 3: 
# 
#  
# Input: nums1 = [-1,-1], nums2 = [1,1]
# Output: -1
# Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
# Their dot product is -1. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums1.length, nums2.length <= 500 
#  -1000 <= nums1[i], nums2[i] <= 1000 
#  
#  Related Topics Dynamic Programming 
#  👍 361 👎 8


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxDotProduct(self, s1, s2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(s1), len(s2)
        return self.dfs(m, n, s1, s2, {})

    def dfs(self, i, j, s1, s2, memo):
        if i <= 0 or j <= 0:
            return float('-inf')
        if (i, j) in memo: 
            return memo[(i, j)]

        ans = s1[i - 1] * s2[j - 1] + \
              max(self.dfs(i - 1, j - 1, s1, s2, memo), 0)
        ans = max(ans,
                  self.dfs(i - 1, j, s1, s2, memo),
                  self.dfs(i, j - 1, s1, s2, memo))
        memo[(i, j)] = ans
        return ans


        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        res = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(max(dp[i - 1][j - 1], 0), s1[m - 1] * s2[n - 1])
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                res = max(dp[i][j])
        return res

print(Solution().maxDotProduct([2,1,-2,5], [3,0,-6]))