# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node, st, res = root, [], []

        while node or st:
            if node:
                res.append(node.val)
                st.append(node)
                # if node.left:
                node = node.left
            else:
                tmp = st.pop()
                node = tmp.right

        return res