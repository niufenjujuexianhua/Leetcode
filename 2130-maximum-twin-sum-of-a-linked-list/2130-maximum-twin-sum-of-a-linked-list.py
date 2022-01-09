# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        dummy = ListNode(0, head)
        s = f = dummy
        while f.next and f.next.next:
            s = s.next
            f = f.next.next

        pre = None
        cur = s.next
        s.next = None

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        res = 0
        while head:
            res = max(res, pre.val + head.val)
            head = head.next 
            pre = pre.next 
        return res 


