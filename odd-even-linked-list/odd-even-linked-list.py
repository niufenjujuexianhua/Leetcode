# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        odd = od = ListNode()
        even = ed = ListNode()
        i = 1
        while head:
            nxt = head.next
            head.next = None

            if i % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            i = 1 - i 
            head = nxt

        odd.next = ed.next
        return od.next