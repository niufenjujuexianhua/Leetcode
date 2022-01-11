class Node():
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.pre = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cnt = 0
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.dt = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dt:
            return -1

        node = self.dt[key]
        val = node.val
        self.remove(node)
        self.addtoend(node)
        return val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dt:
            node = self.dt[key]
            self.remove(node)
            del self.dt[key]
            self.cnt -= 1

        self.cnt += 1
        if self.cnt > self.capacity:
            del self.dt[self.head.next.key]
            self.remove(self.head.next)
            self.cnt -= 1

        node = Node(key, value)
        self.addtoend(node)
        self.dt[key] = node

    def remove(self, node):
        pre, nxt = node.pre, node.next
        node.pre = node.next = None
        pre.next = nxt
        nxt.pre = pre

    def addtoend(self, node):
        pre = self.tail.pre
        pre.next = self.tail.pre = None
        pre.next = node
        node.next = self.tail
        node.pre = pre
        self.tail.pre = node