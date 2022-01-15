# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        self.h = self.height(root) - 1
        m, n = self.h + 1, 2 ** (self.h + 1) - 1

        grid = [[''] * n for _ in range(m)]
        self.dfs(root, grid, 0, (n - 1) // 2)
        return grid


    def dfs(self, root, grid, r, c):
        if not root:
            return

        grid[r][c] = str(root.val)
        self.dfs(root.left, grid, r + 1, c - 2 ** (self.h - r - 1))
        self.dfs(root.right, grid, r + 1, c + 2 ** (self.h - r - 1))


    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))