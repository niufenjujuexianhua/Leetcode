class Solution(object):
    def preorder(self, root):
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
        
        res.append(node.val)
        for kid in node.children:
            self.dfs(kid, res)