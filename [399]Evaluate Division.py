# You are given an array of variable pairs equations and an array of real number
# s values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai 
# / Bi = values[i]. Each Ai or Bi is a string that represents a single variable. 
# 
#  You are also given some queries, where queries[j] = [Cj, Dj] represents the j
# th query where you must find the answer for Cj / Dj = ?. 
# 
#  Return the answers to all queries. If a single answer cannot be determined, r
# eturn -1.0. 
# 
#  Note: The input is always valid. You may assume that evaluating the queries w
# ill not result in division by zero and that there is no contradiction. 
# 
#  
#  Example 1: 
# 
#  
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a",
# "c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
#  
# 
#  Example 2: 
# 
#  
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
#  
# 
#  Example 3: 
# 
#  
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"]
# ,["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= equations.length <= 20 
#  equations[i].length == 2 
#  1 <= Ai.length, Bi.length <= 5 
#  values.length == equations.length 
#  0.0 < values[i] <= 20.0 
#  1 <= queries.length <= 20 
#  queries[i].length == 2 
#  1 <= Cj.length, Dj.length <= 5 
#  Ai, Bi, Cj, Dj consist of lower case English letters and digits. 
#  
#  Related Topics Union Find Graph 
#  👍 2942 👎 237


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(list)

        for i, (a, b) in enumerate(equations):
            graph[a].append([b, values[i]])
            graph[b].append([a, 1.0 / values[i]])

        res = []
        for s, e in queries:
            ans = self.dfs(graph, s, e, 1.0, set())
            res.append(ans)
            if ans != -1.0:
                graph[s].append([e, ans])
                graph[e].append([s, 1.0 / ans])
        return res

    def dfs(self, graph, s, e, path, seen):
        if s not in graph or e not in graph or s in seen:
            return -1.0
        if s == e:
            return path

        seen.add(s)
        for nxt in graph[s]:
            tmp = self.dfs(graph, nxt[0], e, path * nxt[1], seen)
            if tmp != -1.0:
                return tmp
        return -1.0

        
# leetcode submit region end(Prohibit modification and deletion)
