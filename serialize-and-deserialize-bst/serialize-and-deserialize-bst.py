# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.preorder(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return self.deser(collections.deque(data.split(',')))


    def deser(self, ls):
        if ls:
            root = ls.popleft()
            if root == '#':
                return None

            root = TreeNode(root)
            root.left = self.deser(ls)
            root.right = self.deser(ls)
            return root

    def preorder(self, root):
        if not root:
            return '#'

        return str(root.val) + ',' + self.preorder(root.left) + ',' + self.preorder(root.right)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans