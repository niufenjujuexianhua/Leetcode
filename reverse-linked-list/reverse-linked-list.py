class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        1 2 3
      p c n nn
        p c n
        """
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre