# There are a total of n courses you have to take, labeled from 0 to n-1. 
# 
#  Some courses may have direct prerequisites, for example, to take course 0 you
#  have first to take course 1, which is expressed as a pair: [1,0] 
# 
#  Given the total number of courses n, a list of direct prerequisite pairs and 
# a list of queries pairs. 
# 
#  You should answer for each queries[i] whether the course queries[i][0] is a p
# rerequisite of the course queries[i][1] or not. 
# 
#  Return a list of boolean, the answers to the given queries. 
# 
#  Please note that if course a is a prerequisite of course b and course b is a 
# prerequisite of course c, then, course a is a prerequisite of course c. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# Output: [false,true]
# Explanation: course 0 is not a prerequisite of course 1 but the opposite is tr
# ue.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2, prerequisites = [], queries = [[1,0],[0,1]]
# Output: [false,false]
# Explanation: There are no prerequisites and each course is independent.
#  
# 
#  Example 3: 
# 
#  
# Input: n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
# Output: [true,true]
#  
# 
#  Example 4: 
# 
#  
# Input: n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
# Output: [false,true]
#  
# 
#  Example 5: 
# 
#  
# Input: n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0
# ],[1,3],[3,0]]
# Output: [true,false,true,false]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= n <= 100 
#  0 <= prerequisite.length <= (n * (n - 1) / 2) 
#  0 <= prerequisite[i][0], prerequisite[i][1] < n 
#  prerequisite[i][0] != prerequisite[i][1] 
#  The prerequisites graph has no cycles. 
#  The prerequisites graph has no repeated edges. 
#  1 <= queries.length <= 10^4 
#  queries[i][0] != queries[i][1] 
#  
#  Related Topics Graph 
#  👍 312 👎 16


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        graph = collections.defaultdict(list)

        for pre,cour in prerequisites:
            graph[pre].append(cour)

        res = []
        for a, b in queries:
            if self.dfs(graph, a, b, set()):
                graph[a].append(b)
                res.append(True)
            else:
                res.append(False)
        return res

    def dfs(self, graph, a, b, seen):
        if a == b:
            return True

        seen.add(a)
        for nxt in graph[a]:
            if nxt not in seen:
                if self.dfs(graph, nxt, b, seen):
                    return True
        return False
        
# leetcode submit region end(Prohibit modification and deletion)
