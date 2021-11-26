class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = set()
        self.dfs(root, collections.defaultdict(int), res)
        return res

    def dfs(self, root, dt, res):
        if not root:
            return '#'

        lt = self.dfs(root.left, dt, res)
        rt = self.dfs(root.right, dt, res)

        # encoding = lt + ',' + str(root.val) + ',' + rt
        encoding = lt + ',' + rt + ',' + str(root.val)

        # if encoding in dt:
        if dt[encoding] == 1:
                res.add(root)
        dt[encoding] += 1

        return encoding