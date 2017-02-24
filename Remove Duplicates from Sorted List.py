# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        first = head

        while first.next != None:
            second = first.next
            if first.val == second.val:
                first.next = second.next
            else:
                first = first.next
        return head


class Solution2(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = curr = head
        while curr:
            if pre.val != curr.val:
                pre.next = curr
                pre = curr
            else:
                pre.next = curr.next
            curr = curr.next
        return head

if __name__ == '__main__':
    result = Solution().deleteDuplicates()
    print(result)