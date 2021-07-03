class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        hq = []
        for head in lists:
            if head:
                heapq.heappush(hq, (head.val, head))
        
        dummy = cur = ListNode(0)
        while hq:
            v, node = heapq.heappop(hq)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(hq, (node.next.val, node.next))
        
        return dummy.next 