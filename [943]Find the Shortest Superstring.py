# Given an array A of strings, find any smallest string that contains each strin
# g in A as a substring. 
# 
#  We may assume that no string in A is substring of another string in A. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["alex","loves","leetcode"]
# Output: "alexlovesleetcode"
# Explanation: All permutations of "alex","loves","leetcode" would also be accep
# ted.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
# Output: "gctaagttcatgcatc" 
# 
#  
#  
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 12 
#  1 <= A[i].length <= 20 
#  
# 
#  
#  
#  Related Topics Dynamic Programming 
#  👍 434 👎 73


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """

        def overlap(p, n):
            l = min(len(p), len(n))
            for i in range(l - 1, -1, -1):
                if p[len(p) - i:] == n[:i]:
                    return i
            return 0

        l = len(A)
        dist = [[0] * l for _ in range(l)]
        for i in range(l):
            for j in range(i + 1, l):
                dist[i][j] = overlap(A[i], A[j])
                dist[j][i] = overlap(A[j], A[i])

        dp = [[0] * l for _ in range(1 << l)]  # total overlap
        parent = [[None] * l for _ in range(1 << l)]

        for mask in range(1 << l):
            for bit in range(l):
                if mask & (1 << bit):
                    pmask = mask ^ (1 << bit)
                    if pmask == 0:
                        continue
                    for pbit in range(l):
                        if pmask & (1 << pbit):
                            if dp[pmask][pbit] + dist[pbit][bit] >= dp[mask][bit]:
                                dp[mask][bit] = dp[pmask][pbit] + dist[pbit][bit]
                                parent[mask][bit] = pbit

        mask = (1 << l) - 1
        bit = dp[mask].index(max(dp[mask]))
        idxList = []
        while bit is not None:
            idxList.append(bit)
            bit, mask = parent[mask][bit], mask ^ (1 << bit)
        idxList = idxList[::-1]

        resList = []
        for i in range(len(idxList)):
            if i == 0:
                resList.append(A[idxList[i]])
            else:
                resList.append(A[idxList[i]][dist[idxList[i - 1]][idxList[i]]:])
        return ''.join(resList)
        
# leetcode submit region end(Prohibit modification and deletion)
