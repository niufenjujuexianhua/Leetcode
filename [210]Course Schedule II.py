# There are a total of n courses you have to take labelled from 0 to n - 1. 
# 
#  Some courses may have prerequisites, for example, if prerequisites[i] = [ai, 
# bi] this means you must take the course bi before the course ai. 
# 
#  Given the total number of courses numCourses and a list of the prerequisite p
# airs, return the ordering of courses you should take to finish all courses. 
# 
#  If there are many valid answers, return any of them. If it is impossible to f
# inish all courses, return an empty array. 
# 
#  
#  Example 1: 
# 
#  
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you shou
# ld have finished course 0. So the correct course order is [0,1].
#  
# 
#  Example 2: 
# 
#  
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you shou
# ld have finished both courses 1 and 2. Both courses 1 and 2 should be taken afte
# r you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3
# ].
#  
# 
#  Example 3: 
# 
#  
# Input: numCourses = 1, prerequisites = []
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= numCourses <= 2000 
#  0 <= prerequisites.length <= numCourses * (numCourses - 1) 
#  prerequisites[i].length == 2 
#  0 <= ai, bi < numCourses 
#  ai != bi 
#  All the pairs [ai, bi] are distinct. 
#  
#  Related Topics Depth-first Search Breadth-first Search Graph Topological Sort
#  
#  👍 3121 👎 156


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        import collections
        indegree = [0] * numCourses
        graph = collections.defaultdict(set)

        for cour, pre in prerequisites:
            if pre in graph[cour]:
                return []
            indegree[cour] += 1
            graph[pre].add(cour)

        ## BFS
        dq = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        ls = []
        while dq:
            pre = dq.popleft()
            ls.append(pre)
            for cour in graph[pre]:
                indegree[cour] -= 1
                if indegree[cour] == 0:
                    dq.append(cour)
        return ls if not sum(indegree) else []

        ## DFS
        seen, ls = [0] * numCourses, ls
        for pre in range(numCourses):
            if indegree[pre] == 0:
                if self.dfs(graph, pre, seen, ls):
                    return []
        return ls if len(ls) == numCourses else []


    def dfs(self, graph, pre, seen, ls):
        if seen[pre] == -1:
            return True
        if seen[pre] == 1:
            return False
        seen[pre] = -1

        for cour in graph[pre]:
            if self.dfs(graph, cour, seen, ls):
                return True
        seen[pre] = 1
        ls.append(pre)
        return False
# print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
# print(Solution().findOrder(8, [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]))

# leetcode submit region end(Prohibit modification and deletion)
