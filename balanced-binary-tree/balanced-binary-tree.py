class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dt = {}
        node, st = root, []

        while node or st:
            while node:
                st.append(node)
                if node.left:
                    node = node.left
                else:
                    node = node.right

            node = st.pop()
            lt, rt = dt.get(node.left, 0), dt.get(node.right, 0)
            if abs(lt - rt) > 1:
                return False
            
            dt[node] = max(lt, rt) + 1 
            if st and st[-1].left == node:
                node = st[-1].right
            else:
                node = None
        return True 