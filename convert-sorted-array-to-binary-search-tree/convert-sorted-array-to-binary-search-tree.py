# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        s, e = 0, len(nums) - 1
        return self.dfs(nums, s, e)

    def dfs(self, nums, s, e):
        if s == e:
            return TreeNode(nums[s])
        if s > e:
            return
        m = s + (e - s) // 2
        root = TreeNode(nums[m])
        root.left = self.dfs(nums, s, m - 1)
        root.right = self.dfs(nums, m + 1, e)
        return root
        