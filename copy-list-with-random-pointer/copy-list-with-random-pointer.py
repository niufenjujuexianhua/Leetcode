"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return 
        dt = {}
        cur = head
        while cur:
            if cur not in dt:
                dt[cur] = Node(cur.val)

            if cur.next:
                if cur.next not in dt:
                    dt[cur.next] = Node(cur.next.val)
                dt[cur].next = dt[cur.next]

            if cur.random:
                if cur.random not in dt:
                    dt[cur.random] = Node(cur.random.val)
                dt[cur].random = dt[cur.random]
            cur = cur.next
        return dt[head]