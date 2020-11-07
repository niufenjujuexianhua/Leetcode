# Given an array arr of positive integers, consider all binary trees such that: 
# 
# 
#  
#  Each node has either 0 or 2 children; 
#  The values of arr correspond to the values of each leaf in an in-order traver
# sal of the tree. (Recall that a node is a leaf if and only if it has 0 children.
# ) 
#  The value of each non-leaf node is equal to the product of the largest leaf v
# alue in its left and right subtree respectively. 
#  
# 
#  Among all possible binary trees considered, return the smallest possible sum 
# of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bi
# t integer. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [6,2,4]
# Output: 32
# Explanation:
# There are two possible trees.  The first has non-leaf node sum 36, and the sec
# ond has non-leaf node sum 32.
# 
#     24            24
#    /  \          /  \
#   12   4        6    8
#  /  \               / \
# 6    2             2   4
#  
# [i, j] = node val and largest val
#  
#  Constraints: 
# 
#  
#  2 <= arr.length <= 40 
#  1 <= arr[i] <= 15 
#  It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is
#  less than 2^31). 
#  Related Topics Dynamic Programming Stack Tree 
#  👍 1585 👎 123


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = [[float('inf')] * n for _ in range(n)]
        maxn = [[-float('inf')] * n for _ in range(n)]

        for j in range(n):
            for i in range(j, -1, -1):
                if i == j:
                    maxn[i][j] = arr[i]
                else:
                    for k in range(i, j):
                        maxn[i][j] = max(maxn[i][j], maxn[i][k], maxn[k + 1][j])


        for j in range(n):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = 0
                elif i + 1 == j:
                    dp[i][j] = arr[i] * arr[j]
                else:
                    for k in range(i, j):
                        val = maxn[i][k] * maxn[k + 1][j]

                        dp[i][j] = min(dp[i][j],
                                       val + dp[i][k] + dp[k + 1][j])
        return dp[0][-1]



    # def dfs(self, arr, i, j, memo):
    #     if i == j:
    #         return (arr[i], arr[i])
    #
    #     if (i, j) in memo:
    #         return memo[i, j]
    #
    #     ans = float('inf')
    #     for k in range(i, j + 1):
    #         lt = self.dfs(arr, i, k, memo)
    #         rt = self.dfs(arr, k + 1, j, memo)
    #
    #         nodeval = lt[1] * rt[1]
    #         largeval = max(lt[1], rt[1])
    #         return (nodeval, largeval)




        
# leetcode submit region end(Prohibit modification and deletion)
