class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val = [root.val, float('inf')]
        self.dfs(root, val)
        if val[1] == float('inf'):
            return -1
        return val[1]

    def dfs(self, root, val):
        # print(root.val)
        if not root:
            return
        if val[1] > root.val > val[0]:
            val[1] = root.val
        elif root.val == val[0]:
            self.dfs(root.left, val)
            self.dfs(root.right, val)