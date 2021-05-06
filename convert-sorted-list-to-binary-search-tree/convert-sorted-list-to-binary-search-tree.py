class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.dfs(head)

    def dfs(self, head):
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        if not head.next.next:
            root = TreeNode(head.next.val)
            root.left = TreeNode(head.val)
            return root

        pre, slow, fast = head, head, head
        while fast.next and fast.next.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        nxt = slow.next
        pre.next = slow.next = None

        root = TreeNode(slow.val)
        root.left = self.dfs(head)
        root.right = self.dfs(nxt)
        return root