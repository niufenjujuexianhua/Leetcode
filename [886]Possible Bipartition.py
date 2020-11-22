# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyo
# ne into two groups of any size. 
# 
#  Each person may dislike some other people, and they should not go into the sa
# me group. 
# 
#  Formally, if dislikes[i] = [a, b], it means it is not allowed to put the peop
# le numbered a and b into the same group. 
# 
#  Return true if and only if it is possible to split everyone into two groups i
# n this way. 
# 
#  
# 
#  
#  
#  
#  
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
#  
# 
#  
#  Example 3: 
# 
#  
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#  
#  
#  
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= N <= 2000 
#  0 <= dislikes.length <= 10000 
#  dislikes[i].length == 2 
#  1 <= dislikes[i][j] <= N 
#  dislikes[i][0] < dislikes[i][1] 
#  There does not exist i != j for which dislikes[i] == dislikes[j]. 
#  Related Topics Depth-first Search Graph 
#  👍 1187 👎 32


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        for a, b in dislikes:
            graph[a].add(b)
            graph[b].add(a)

        seen = collections.defaultdict(int)
        for i in range(1, n + 1):
            if seen[i] == 0:
                if not self.dfs(graph, seen, i, 1, n):
                    return False
        return True

    def dfs(self, graph, seen, node, val, n):
        if seen[node] != 0:
            return seen[node] == val

        seen[node] = val
        for nxt in graph[node]:
            if not self.dfs(graph, seen, nxt, -val, n):
                return False
        return True
        
# leetcode submit region end(Prohibit modification and deletion)
