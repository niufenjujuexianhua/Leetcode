# Given n, how many structurally unique BST's (binary search trees) that store v
# alues 1 ... n? 
# 
#  Example: 
# 
#  
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 19 
#  
#  Related Topics Dynamic Programming Tree 
#  👍 4076 👎 150


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        return len(self.dfs(n))

    def dfs(self, i):
        trees = []
        print(i)
        if i <= 0 or i > self.n:
            return trees

        for j in range(1, self.n):
            root = TreeNode(j)
            for lt in self.dfs(j - 1):
                for rt in self.dfs(j + 1):
                    root.left = lt
                    root.right = rt
                    trees.append(root)
        return trees
print(Solution().numTrees(3))
        
# leetcode submit region end(Prohibit modification and deletion)
