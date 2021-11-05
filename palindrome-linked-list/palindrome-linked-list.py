# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        self.head = head
        return self.rec(head)

    def rec(self, cur):
        if not cur:
            return True

        ans = self.rec(cur.next)

        equal = self.head.val == cur.val
        self.head = self.head.next

        return equal and ans
        