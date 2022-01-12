class Solution(object):
    def findOrder(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        import collections
        g = collections.defaultdict(set)
        indegree = [0] * n
        seen = [0] * n

        for cour, pre in prerequisites:
            g[pre].add(cour)
            indegree[cour] += 1

        path = []
        for pre in range(n):
            if seen[pre] == 0 and indegree[pre] == 0:
                # path = []
                if not self.dfs(g, seen, pre, path):
                    return [] 
                # res.extend(path[::-1])
        if len(path) != n:
            return [] 
        return path[::-1]

    def dfs(self, g, seen, pre, path):
        # 0 not visited  1 visited  -1 being visited
        if seen[pre] == 1:
            return True
        if seen[pre] == -1:
            return False
        seen[pre] = -1

        for nxt in g[pre]:
            if not self.dfs(g, seen, nxt, path):
                return False 
        seen[pre] = 1
        path.append(pre)
        return True 