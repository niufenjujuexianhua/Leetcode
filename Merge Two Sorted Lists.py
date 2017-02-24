# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            if l1.val > l2.val:
                l1, b = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
            
        return l1 or l2
        
    


class Solution2(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(None)
        
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1.next
            else:
                p.next = l2
                l2.next
            p.next
        if l1: p.next = l1
        if l2: p.next = l2
        return dummy.next

        
if __name__ == '__main__':
    result = Solution().mergeTwoLists()
    print(result)