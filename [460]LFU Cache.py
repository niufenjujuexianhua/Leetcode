# Design and implement a data structure for a Least Frequently Used (LFU) cache.
#  
# 
#  Implement the LFUCache class: 
# 
#  
#  LFUCache(int capacity) Initializes the object with the capacity of the data s
# tructure. 
#  int get(int key) Gets the value of the key if the key exists in the cache. Ot
# herwise, returns -1. 
#  void put(int key, int value) Update the value of the key if present, or inser
# ts the key if not already present. When the cache reaches its capacity, it shoul
# d invalidate and remove the least frequently used key before inserting a new ite
# m. For this problem, when there is a tie (i.e., two or more keys with the same f
# requency), the least recently used key would be invalidated. 
#  
# 
#  To determine the least frequently used key, a use counter is maintained for e
# ach key in the cache. The key with the smallest use counter is the least frequen
# tly used key. 
# 
#  When a key is first inserted into the cache, its use counter is set to 1 (due
#  to the put operation). The use counter for a key in the cache is incremented ei
# ther a get or put operation is called on it. 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "g
# et"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# 
# Explanation
# // cnt(x) = the use counter for key x
# // cache=[] will show the last used order for tiebreakers (leftmost element is
#   most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalid
# ate 2.
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1
# .
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
#                  // cache=[3,4], cnt(4)=2, cnt(3)=3
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= capacity, key, value <= 104 
#  At most 105 calls will be made to get and put. 
#  
# 
#  
# Follow up: Could you do both operations in O(1) time complexity? Related Topic
# s Design 
#  👍 1960 👎 151


# leetcode submit region begin(Prohibit modification and deletion)
class Node(object):
    def __init__(self, k, v):
        self.prev = None
        self.next = None
        self.key = k
        self.val = v
        self.cnt = 1

class DoublyLinkedList(object):
    def __init__(self):
        self.head = Node(0, 0) # head is a dummy head node
        self.tail = Node(0, 0) # tail is a dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1

    def remove_tail(self):
        old_tail = self.tail.prev
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        self.size -= 1
        return old_tail

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.node_dict = {}
        self.freq_dict = collections.defaultdict(DoublyLinkedList)
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_dict:
            return -1
        else:
            node = self.node_dict[key]
            old_cnt = node.cnt
            node.cnt += 1
            self.freq_dict[old_cnt].remove_node(node)
            self.freq_dict[node.cnt].add_to_head(node)
            if old_cnt == self.min_freq and self.freq_dict[old_cnt].size == 0:
                self.min_freq += 1
            return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0:
            return
        if key not in self.node_dict:
            node = Node(key, value)
            self.node_dict[key] = node
            if self.size != self.capacity:
                self.freq_dict[1].add_to_head(node)
                self.size += 1
            else:
                old_tail = self.freq_dict[self.min_freq].remove_tail()
                self.node_dict.pop(old_tail.key)
                self.freq_dict[1].add_to_head(node)
            self.min_freq = 1
        else:
            node = self.node_dict[key]
            node.val = value
            old_cnt = node.cnt
            node.cnt += 1
            self.freq_dict[old_cnt].remove_node(node)
            self.freq_dict[node.cnt].add_to_head(node)
            if old_cnt == self.min_freq and self.freq_dict[old_cnt].size == 0:
                self.min_freq += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
