class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        1 2 _ 3 4 5 6
      p   c n
        """
        if not head:
            return

        dummy = ListNode()
        dummy.next = head
        pre, cur = dummy, head

        while cur:
            if cur.val == val:
                nxt = cur.next
                cur.next = None
                pre.next = nxt
                cur = nxt
            else:
                pre = pre.next
                cur = cur.next 
        return dummy.next