class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0 
        ans = 1 
        if root.children:
            ans += max(self.maxDepth(ch) for ch in root.children)
        return ans 