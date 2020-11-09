# There are N piles of stones arranged in a row. The i-th pile has stones[i] sto
# nes. 
# 
#  A move consists of merging exactly K consecutive piles into one pile, and the
#  cost of this move is equal to the total number of stones in these K piles. 
# 
#  Find the minimum cost to merge all piles of stones into one pile. If it is im
# possible, return -1. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: stones = [3,2,4,1], K = 2
# Output: 20
# Explanation: 
# We start with [3, 2, 4, 1].
# We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
# We merge [4, 1] for a cost of 5, and we are left with [5, 5].
# We merge [5, 5] for a cost of 10, and we are left with [10].
# The total cost was 20, and this is the minimum possible.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: stones = [3,2,4,1], K = 3
# Output: -1
# Explanation: After any merge operation, there are 2 piles left, and we can't m
# erge anymore.  So the task is impossible.
#  
# 
#  
#  Example 3: 
# 
#  
# Input: stones = [3,5,1,2,6], K = 3
# Output: 25
# Explanation: 
# We start with [3, 5, 1, 2, 6].
# We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
# We merge [3, 8, 6] for a cost of 17, and we are left with [17].
# The total cost was 25, and this is the minimum possible.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= stones.length <= 30 
#  2 <= K <= 30 
#  1 <= stones[i] <= 100 
#  
#  
#  
#  Related Topics Dynamic Programming 
#  👍 758 👎 51


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mergeStones(self, stones, K):
        n = len(stones)
        if (n-1) % (K-1) != 0:
            return -1

        dp = [[0]*n for _ in range(n)]

        sums = [0]*(n+1)
        for i in range(1,n+1):
            sums[i] = sums[i-1]+stones[i-1]

        for length in range(K,n+1):
            for i in range(n-length+1):
                j = i+length-1
                dp[i][j] = float('inf')
                for t in range(i,j,K-1):
                    dp[i][j] = min(dp[i][j], dp[i][t]+dp[t+1][j])
                if (j-i)%(K-1)==0:
                    dp[i][j] += sums[j+1]-sums[i]
        return dp[0][n-1]



# leetcode submit region end(Prohibit modification and deletion)
