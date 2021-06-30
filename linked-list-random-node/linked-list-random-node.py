class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        sz = 1
        val = 0
        head = self.head
        while head:
            if random.random() < 1.0 / sz:
                val = head.val
            head = head.next
            sz += 1
        return val 