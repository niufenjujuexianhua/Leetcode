class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def dfs(self, preorder, pi, pj, inorder, ii, ij):
        if pi > pj:
            return
        if pi == pj:
            return TreeNode(preorder[pi])

        root = TreeNode(preorder[pi])
        idx = inorder.index(preorder[pi])
        lt, rt = idx - ii, ij - idx

        root.left = self.dfs(preorder, pi + 1, pi + lt, inorder, ii, idx - 1)
        root.right = self.dfs(preorder, pi + lt + 1, pj, inorder, idx + 1, ij)
        return root