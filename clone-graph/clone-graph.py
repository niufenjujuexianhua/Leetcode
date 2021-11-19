class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        dt = {}
        self.dfs(node, dt)
        return dt[node]
        
    def dfs(self, node, dt):
        if not node:
            return 
        if node in dt:
            return dt[node]
        
        dt[node] = Node(node.val, [])
        for nei in node.neighbors:
            dt[node].neighbors.append(self.dfs(nei, dt))
        
        return dt[node]