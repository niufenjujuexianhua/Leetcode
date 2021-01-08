# There are n items each belonging to zero or one of m groups where group[i] is 
# the group that the i-th item belongs to and it's equal to -1 if the i-th item be
# longs to no group. The items and the groups are zero indexed. A group can have n
# o item belonging to it. 
# 
#  Return a sorted list of the items such that: 
# 
#  
#  The items that belong to the same group are next to each other in the sorted 
# list. 
#  There are some relations between these items where beforeItems[i] is a list c
# ontaining all the items that should come before the i-th item in the sorted arra
# y (to the left of the i-th item). 
#  
# 
#  Return any solution if there is more than one solution and return an empty li
# st if there is no solution. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[
# 6],[3,6],[],[],[]]
# Output: [6,3,4,1,5,2,0,7]
#  
# 
#  Example 2: 
# 
#  
# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[
# 6],[3],[],[4],[]]
# Output: []
# Explanation: This is the same as example 1 except that 4 needs to be before 6 
# in the sorted list.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= m <= n <= 3*10^4 
#  group.length == beforeItems.length == n 
#  -1 <= group[i] <= m-1 
#  0 <= beforeItems[i].length <= n-1 
#  0 <= beforeItems[i][j] <= n-1 
#  i != beforeItems[i][j] 
#  beforeItems[i] does not contain duplicates elements. 
#  
#  Related Topics Depth-first Search Graph Topological Sort 
#  👍 328 👎 60


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        group_graph = defaultdict(list)
        item_graph = defaultdict(list)
        group_indegree = defaultdict(int)
        item_indegree = defaultdict(int)

        for u in range(n):
            if group[u] == -1:
                group[u] = m
                m += 1

        for v in range(n):
            for u in beforeItems[v]:
                if group[u] != group[v]:
                    group_graph[group[u]].append(group[v])
                    group_indegree[group[v]] += 1
                item_graph[u].append(v)
                item_indegree[v] += 1

        group_order = self.bfs(group_graph, group_indegree, m)
        item_order = self.bfs(item_graph, item_indegree, n)
        if not group_order or not item_order: return []

        groups = defaultdict(list)
        for item in item_order:
            groups[group[item]].append(item)

        res = []
        for g in group_order:
            res.extend(groups[g])
        return res

    def bfs(self, graph, indegree, n):
        nodes = [i for i in range(n) if indegree[i] == 0]
        dq, seen, order = deque(nodes), set(nodes), []
        while dq:
            u = dq.popleft()
            order.append(u)
            for v in graph[u]:
                if v not in seen:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        dq.append(v)
        return order if len(order) == n else []

# leetcode submit region end(Prohibit modification and deletion)
