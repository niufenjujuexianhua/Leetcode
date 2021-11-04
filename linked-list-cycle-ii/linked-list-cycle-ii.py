# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next :
            return 
        
    #         slow, fast = head, head
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next
    #     if slow == fast:
    #         slow2 = head
    #         while slow != slow2:
    #             slow = slow.next
    #             slow2 = slow2.next
    #         return slow

        entry = slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                while entry != slow:
                    slow, entry = slow.next, entry.next
                return entry
        return 