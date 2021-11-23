class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, s, e):
        if s > e:
            return
        if s == e:
            return TreeNode(nums[s])

        m = s + (e - s) // 2
        root = TreeNode(nums[m])

        root.left = self.dfs(nums, s, m - 1)
        root.right = self.dfs(nums, m + 1, e)
        return root