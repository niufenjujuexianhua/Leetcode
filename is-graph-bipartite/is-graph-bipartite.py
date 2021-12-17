class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        colors = {}
        for i in range(len(graph)):
            if i not in colors:
                if not self.dfs(graph, i, 0, colors):
                    return False 
        return True 

    def dfs(self, graph, i, c, colors):
        if i in colors:
            return colors[i] == c 
        
        colors[i] = c 
        for nxt in graph[i]:
            if not self.dfs(graph, nxt, 1 - c, colors):
                return False
        return True