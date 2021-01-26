# An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given
#  as graph. 
# 
#  graph.length = N, and j != i is in the list graph[i] exactly once, if and onl
# y if nodes i and j are connected. 
# 
#  Return the length of the shortest path that visits every node. You may start 
# and stop at any node, you may revisit nodes multiple times, and you may reuse ed
# ges. 
# 
#  
# 
#  
#  
# 
#  Example 1: 
# 
#  
# Input: [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3] 
# 
#  Example 2: 
# 
#  
# Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= graph.length <= 12 
#  0 <= graph[i].length < graph.length 
#  
#  Related Topics Dynamic Programming Breadth-first Search 
#  👍 718 👎 76


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        import collections
        n = len(graph)
        target = (1 << n) - 1
        q = collections.deque([(0, 1 << i, i) for i in range(n)])
        seen = set()
        while q:
            steps, state, node = q.popleft()
            if state == target: return steps
            if (state, node) in seen: continue

            seen.add((state, node))
            for nxt in graph[node]:
                q.append((steps + 1, state | (1 << nxt), nxt))
        return -1
    
# print(Solution().shortestPathLength([[1,2,3],[0],[0],[0]] ))
# leetcode submit region end(Prohibit modification and deletion)
