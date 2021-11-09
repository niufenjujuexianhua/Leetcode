class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        st = [[root, target]]
        while st:
            node, val = st.pop()
            # print(node.val, val)
            if not node.left and not node.right and node.val == val:
                return True
            if node.left:
                st.append([node.left, val - node.val])
            if node.right:
                st.append([node.right, val - node.val])
        return False