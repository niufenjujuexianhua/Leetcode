class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if not root: return 0
        dt = collections.defaultdict(int)
        dt[0], res = 1, [0]
        self.dfs(root, 0, targetSum, dt, res)
        return res[0]

    def dfs(self, root, cur, target, dt, res):
        if not root:
            return 0

        cur += root.val
        res[0] += dt[cur - target]
        dt[cur] += 1
        self.dfs(root.left, cur, target, dt, res)
        self.dfs(root.right, cur, target, dt, res)
        dt[cur] -= 1
        