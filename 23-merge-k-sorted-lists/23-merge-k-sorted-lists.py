class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        hq = []
        for head in lists:
            if head:
                heapq.heappush(hq, (head.val, head))

        dummy = cur = ListNode(0)
        while hq:
            val, head = heapq.heappop(hq)

            cur.next = ListNode(val)
            cur = cur.next

            if head.next:
                heapq.heappush(hq, (head.next.val, head.next))

        return dummy.next