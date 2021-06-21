class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not head:
            return []
        i, cur, st, dt = 0, head, [], collections.defaultdict(set)
        while cur:
            while st and st[-1][1] < cur.val:
                dt[cur.val].add(st.pop()[0])
            st.append((i, cur.val))
            i += 1
            cur = cur.next

        res = [0] * i
        for val, idx in dt.items():
            for i in idx:
                res[i] = val
        return res