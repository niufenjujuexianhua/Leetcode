# You are given the root of a binary tree with n nodes, where each node is uniqu
# ely assigned a value from 1 to n. You are also given a sequence of n values voya
# ge, which is the desired pre-order traversal of the binary tree. 
# 
#  Any node in the binary tree can be flipped by swapping its left and right sub
# trees. For example, flipping node 1 will have the following effect: 
# 
#  Flip the smallest number of nodes so that the pre-order traversal of the tree
#  matches voyage. 
# 
#  Return a list of the values of all flipped nodes. You may return the answer i
# n any order. If it is impossible to flip the nodes in the tree to make the pre-o
# rder traversal match voyage, return the list [-1]. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2], voyage = [2,1]
# Output: [-1]
# Explanation: It is impossible to flip the nodes such that the pre-order traver
# sal matches voyage.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,3], voyage = [1,3,2]
# Output: [1]
# Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal m
# atches voyage. 
# 
#  Example 3: 
# 
#  
# Input: root = [1,2,3], voyage = [1,2,3]
# Output: []
# Explanation: The tree's pre-order traversal already matches voyage, so no node
# s need to be flipped.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is n. 
#  n == voyage.length 
#  1 <= n <= 100 
#  1 <= Node.val, voyage[i] <= n 
#  All the values in the tree are unique. 
#  All the values in voyage are unique. 
#  
#  Related Topics Tree Depth-first Search 
#  👍 522 👎 209


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(1)
root.left = TreeNode(5)
root.right = TreeNode(6)
root.left.left = TreeNode(7)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.res, self.i = [], 0
        self.dfs(root, voyage)
        return self.res

    def dfs(self, root, voyage):
        if not root or self.i >= len(voyage) or self.res == [-1]:
            return
        if root.val != voyage[self.i]:
            self.res = [-1]
            return

        self.i += 1
        if root.left and root.left.val != voyage[self.i]:
            self.res.append(root.val)
            self.dfs(root.right, voyage)
            self.dfs(root.left, voyage)
        else:
            self.dfs(root.left, voyage)
            self.dfs(root.right, voyage)


print(Solution().flipMatchVoyage(root, [1,5,2,6,3,4,7]))




    # leetcode submit region end(Prohibit modification and deletion)
