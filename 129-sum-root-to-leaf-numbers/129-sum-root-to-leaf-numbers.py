class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root, 0)
        return self.res 

    def dfs(self, node, cur):
        if not node:
            return
        cur = cur * 10 + node.val
        if not node.left and not node.right:
            self.res += cur
        self.dfs(node.left, cur)
        self.dfs(node.right, cur)