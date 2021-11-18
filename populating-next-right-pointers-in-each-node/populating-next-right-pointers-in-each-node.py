class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.dfs(root)
        return root 

    def dfs(self, node):
        if not node:
            return
        if node.left:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left

        self.dfs(node.left)
        self.dfs(node.right)