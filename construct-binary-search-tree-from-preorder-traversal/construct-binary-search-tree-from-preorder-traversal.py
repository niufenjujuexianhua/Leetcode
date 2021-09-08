class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        return self.recur(preorder[::-1], float('inf'))

    def recur(self, preorder, bound):
        if not preorder or preorder[-1] > bound:
            return None

        root = TreeNode(preorder.pop())
        root.left = self.recur(preorder, root.val)
        root.right = self.recur(preorder, bound)
        return root 