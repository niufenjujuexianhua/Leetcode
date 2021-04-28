class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [] 
        self.dfs(root, targetSum, res, [])
        return res 

    def dfs(self, root, target, res, path):
        if not root:
            return
        if not root.left and not root.right:
            if target == root.val:
                res.append(path + [root.val])
            return

        self.dfs(root.left, target - root.val, res, path + [root.val])
        self.dfs(root.right, target - root.val, res, path + [root.val])
        
        
        