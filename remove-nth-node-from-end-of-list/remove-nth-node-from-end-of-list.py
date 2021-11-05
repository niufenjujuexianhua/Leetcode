class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return

        dummy = ListNode()
        dummy.next = head
        s = f = dummy
        for i in range(n):
            f = f.next

        while f and f.next:
            s, f = s.next, f.next

        s.next = s.next.next
        return dummy.next