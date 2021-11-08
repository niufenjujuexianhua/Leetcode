# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        

        d = ListNode
        d.next = head

        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next

        k = k % cnt
        if k == 0:
            return head 
        
        s = f = d
        for _ in range(k):
            f = f.next
        while f and f.next:
            s, f = s.next, f.next

        newhead = s.next
        s.next = None
        f.next = d.next
        return newhead