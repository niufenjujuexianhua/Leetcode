class Node(object):
    def __init__(self, val):
        self.pre = None
        self.next = None
        self.val = val

class MyLinkedList(object):
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.pre = self.head

        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        0 1 2 3
        1 2 3 4
      s f
        """
        if index >= self.size:
            return -1 
        cur = self.head.next 
        for i in range(index):
            cur = cur.next 
        return cur.val 


    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self._addNode(self.head, self.head.next, Node(val))
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self._addNode(self.tail.pre, self.tail, Node(val))
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return 
        slow, fast = self.head, self.head.next
        for i in range(index):
            # print(i, index, slow.val, fast.val)
            slow, fast = fast, fast.next
        
        self._addNode(slow, fast, Node(val))
        self.size += 1
        
    def _addNode(self, p, n, node):
        node.pre = p 
        node.next = n 
        p.next = node 
        n.pre = node 
    
    
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.size:
            return 
        slow, fast = self.head, self.head.next
        for i in range(index):
            slow, fast = fast, fast.next
        
        nxt = fast.next 
        slow.next = nxt 
        nxt.pre = slow 
        self.size -= 1 