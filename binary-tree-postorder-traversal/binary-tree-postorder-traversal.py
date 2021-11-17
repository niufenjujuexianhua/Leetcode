# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node, st, res = root, [], []

        while node or st:
            while node:
                st.append(node)
                if node.left:
                    node = node.left
                else:
                    node = node.right

            node = st.pop()
            res.append(node.val)
            if st and st[-1].left == node:
                node = st[-1].right
            else:
                node = None

        return res
        
