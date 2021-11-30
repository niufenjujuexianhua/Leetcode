class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        return self.dfs(node, {})

    def dfs(self, node, dt):
        if not node:
            return
        if node in dt:
            return dt[node]

        # dt[node] = Node(node.val, [])
        # for nxt in node.neighbors:
        #     dt[node].neighbors.append(self.dfs(nxt, dt))
        #
        # return dt[node]

        nnode = Node(node.val, [])
        dt[node] = nnode
        for nxt in node.neighbors:
            nnode.neighbors.append(self.dfs(nxt, dt))
        
        return nnode