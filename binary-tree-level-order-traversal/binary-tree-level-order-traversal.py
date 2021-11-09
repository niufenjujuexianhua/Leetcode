# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        bfs = collections.deque([root])
        res = []
        while bfs:
            size = len(bfs)
            res.append([])
            for _ in range(size):
                node = bfs.popleft()
                res[-1].append(node.val)

                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
        return res
        