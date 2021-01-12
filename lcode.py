# class Solution(object):
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colors = [-1] * n

        for i in range(n):
            if colors[i] == -1:
                if not self.dfs(graph, i, colors, 1):
                    return False
        return True

    def dfs(self, graph, i, colors, col):
        colors[i] = col
        for nxt in graph[i]:
            if colors[nxt] == col:
                return False
            elif colors[nxt] == 1 - col:
                continue
            if not self.dfs(graph, nxt, colors, 1 - col):
                return False
        return True

print(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]]))