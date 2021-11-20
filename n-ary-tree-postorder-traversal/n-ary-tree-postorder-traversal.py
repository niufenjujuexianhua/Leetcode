class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, node, res):
        if not node:
            return 
        
        for child in node.children:
            self.dfs(child, res)
        res.append(node.val)