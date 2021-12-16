class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        import collections
        g = collections.defaultdict(set)

        for c, p in prerequisites:
            g[p].add(c)

        seen = [0] * numCourses
        for cour in range(numCourses):
            if seen[cour] == 0:
                if not self.dfs(g, cour, seen):
                    return False
        return True

    def dfs(self, g, cour, seen):
        if seen[cour] == 1:
            return True
        if seen[cour] == -1:
            return False

        seen[cour] = -1
        for nxt in g[cour]:
            if not self.dfs(g, nxt, seen):
                return False

        seen[cour] = 1
        return True