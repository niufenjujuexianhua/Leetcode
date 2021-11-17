class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        cur, st = root, []
        while cur or st:
            while cur:
                st.append(cur)
                if cur.left:
                    cur = cur.left
                else:
                    cur = cur.right

            cur = st.pop()
            res.append(cur.val)
            if st and st[-1].left == cur:
                cur = st[-1].right
            else:
                cur = None
        return res