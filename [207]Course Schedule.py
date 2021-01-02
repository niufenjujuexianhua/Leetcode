# There are a total of numCourses courses you have to take, labeled from 0 to nu
# mCourses-1. 
# 
#  Some courses may have prerequisites, for example to take course 0 you have to
#  first take course 1, which is expressed as a pair: [0,1] 
# 
#  Given the total number of courses and a list of prerequisite pairs, is it pos
# sible for you to finish all courses? 
# 
#  
#  Example 1: 
# 
#  
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is poss
# ible.
#  
# 
#  Example 2: 
# 
#  
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take c
# ourse 0 you should
#              also have finished course 1. So it is impossible.
#  
# 
#  
#  Constraints: 
# 
#  
#  The input prerequisites is a graph represented by a list of edges, not adjace
# ncy matrices. Read more about how a graph is represented. 
#  You may assume that there are no duplicate edges in the input prerequisites. 
# 
#  1 <= numCourses <= 10^5 
#  
#  Related Topics Depth-first Search Breadth-first Search Graph Topological Sort
#  
#  👍 4980 👎 201


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        import collections
        indegree = [0] * numCourses
        graph = collections.defaultdict(set)

        for cour, pre in prerequisites:
            if pre in graph[cour]:
                return False
            indegree[cour] += 1
            graph[pre].add(cour)

        seen = [0] * numCourses
        for pre in range(numCourses):
            if indegree[pre] == 0 and seen[pre] == 0:
                if not self.dfs(graph, pre, seen):
                    return False
        return sum(seen[i] == 1 for i in range(numCourses)) == numCourses

    def dfs(self, graph, pre, seen):
        if seen[pre] == -1:
            return False
        if seen[pre] == 1:
            return True
        seen[pre] = -1
        for cour in graph[pre]:
            if not self.dfs(graph, cour, seen):
                return False
        seen[pre] = 1
        return True
# print(Solution().canFinish(2, [[1,0],[0,1]]))

# leetcode submit region end(Prohibit modification and deletion)
