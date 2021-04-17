# Design a data structure that follows the constraints of a Least Recently Used 
# (LRU) cache. 
# 
#  Implement the LRUCache class: 
# 
#  
#  LRUCache(int capacity) Initialize the LRU cache with positive size capacity. 
# 
#  int get(int key) Return the value of the key if the key exists, otherwise ret
# urn -1. 
#  void put(int key, int value) Update the value of the key if the key exists. O
# therwise, add the key-value pair to the cache. If the number of keys exceeds the
#  capacity from this operation, evict the least recently used key. 
#  
# 
#  Follow up: 
# Could you do get and put in O(1) time complexity? 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 3000 
#  0 <= value <= 104 
#  At most 3 * 104 calls will be made to get and put. 
#  
#  Related Topics Design 
#  👍 8251 👎 340


# leetcode submit region begin(Prohibit modification and deletion)
class ListNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
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
        self.extract(node)
        self.addLast(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dt:
            node = self.dt[key]
            node.val = value
            self.extract(node)
            self.addLast(node)
        else:
            if self.size == self.capacity:
                del self.dt[self.head.next.key]
                self.extract(self.head.next)
                self.size -= 1
            node = ListNode(key, value)
            self.dt[key] = node
            self.addLast(node)
            self.size += 1

    def extract(self, node):
        p, n = node.pre, node.next
        p.next, n.pre = n, p
        node.pre = node.next = None

    def addLast(self, node):
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
