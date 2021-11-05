class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        ha, hb = headA, headB
        while ha != hb:
            if ha == hb:
                return ha

            ha = ha.next if ha else headB
            hb = hb.next if hb else headA

        return hb