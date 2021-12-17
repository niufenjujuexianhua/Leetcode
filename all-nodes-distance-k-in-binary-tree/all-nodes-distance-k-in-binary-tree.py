class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        self.res = []
        self.dfs(root, target, K)
        return self.res

    def dfs(self, node, target, k):
        if not node:
            return -1

        if node == target:
            self.fetch(node, k)
            return 0

        lt = self.dfs(node.left, target, k)
        if lt != -1:
            if lt == k - 1:
                self.res.append(node.val)
            else:
                self.fetch(node.right, k - lt - 2)
            return lt + 1

        rt = self.dfs(node.right, target, k)
        if rt != -1:
            if rt == k - 1:
                self.res.append(node.val)
            else:
                self.fetch(node.left, k - rt - 2)
            return rt + 1

        return -1



    def fetch(self, node, k):
            if not node or k < 0:
                return
            if k == 0:
                self.res.append(node.val)
                return 
            self.fetch(node.left, k - 1)
            self.fetch(node.right, k - 1)