class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        cur, nxtfirst, node = None, None, root
        while node:
            if node.left:
                if not nxtfirst:
                    cur = nxtfirst = node.left
                else:
                    cur.next = node.left
                    cur = cur.next
            if node.right:
                if not nxtfirst:
                    cur = nxtfirst = node.right
                else:
                    cur.next = node.right
                    cur = cur.next 
            
            node = node.next
            if not node:
                cur, nxtfirst, node = None, None, nxtfirst
        
        return root