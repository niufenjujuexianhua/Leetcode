class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        import collections
        g = collections.defaultdict(set)
        indegree = collections.defaultdict(int)

        for c, p in prerequisites:
            indegree[c] += 1
            g[p].add(c)

        seen = [0] * numCourses
        order = []
        for cour in range(numCourses):
            if seen[cour] == 0 and indegree[cour] == 0:
                if not self.dfs(g, cour, seen, order):
                    return []
        if len(order) == numCourses:
            return order[::-1]
        return []

    def dfs(self, g, cour, seen, order):
        if seen[cour] == 1:
            return True
        if seen[cour] == -1:
            return False

        
        seen[cour] = -1

        for nxt in g[cour]:
            if not self.dfs(g, nxt, seen, order):
                return False

        seen[cour] = 1
        order.append(cour)
        return True
