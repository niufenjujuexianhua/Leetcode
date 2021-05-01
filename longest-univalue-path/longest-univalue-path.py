class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.dfs(root, res)
        return res[0]

    def dfs(self, root, res):
        if not root:
            return 0

        lt = self.dfs(root.left, res)
        rt = self.dfs(root.right, res)

        L = R = 0 
        if root.left is not None and root.left.val == root.val:
            L = lt + 1 
        if root.right is not None and root.right.val == root.val:
            R = rt + 1 
        res[0] = max(res[0], L + R)
        return max(L, R)