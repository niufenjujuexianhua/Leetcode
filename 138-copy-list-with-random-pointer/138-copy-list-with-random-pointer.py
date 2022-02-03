"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return 
        self.visited = {}
        self.dfs(head)
        return self.visited[head]
    
    
    def dfs(self, head):
        if head is None: return None
        if head in self.visited:
            return self.visited[head]
        node = Node(head.val)
        
        self.visited[head] = node
        node.next = self.dfs(head.next)
        node.random = self.dfs(head.random)
        return node