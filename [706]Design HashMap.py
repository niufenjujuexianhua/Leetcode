# Design a HashMap without using any built-in hash table libraries. 
# 
#  To be specific, your design should include these functions: 
# 
#  
#  put(key, value) : Insert a (key, value) pair into the HashMap. If the value a
# lready exists in the HashMap, update the value. 
#  get(key): Returns the value to which the specified key is mapped, or -1 if th
# is map contains no mapping for the key. 
#  remove(key) : Remove the mapping for the value key if this map contains the m
# apping for the key. 
#  
# 
#  
# Example: 
# 
#  
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);         
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1 
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found) 
#  
# 
#  
# Note: 
# 
#  
#  All keys and values will be in the range of [0, 1000000]. 
#  The number of operations will be in the range of [1, 10000]. 
#  Please do not use the built-in HashMap library. 
#  
#  Related Topics Hash Table Design 
#  👍 1376 👎 152


# leetcode submit region begin(Prohibit modification and deletion)
class Node():
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ls = [Node() for _ in range(1000)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        idx = hash(key) % 1000
        prev = self.ls[idx]
        cur = prev.next
        while cur:
            if cur.key == key:
                cur.val = value
                return
            prev, cur = prev.next, cur.next
        prev.next = Node(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        idx = hash(key) % 1000
        cur = self.ls[idx].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        idx = hash(key) % 1000
        prev = self.ls[idx]
        cur = prev.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                cur.next = None
                return
            prev, cur = prev.next, cur.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# leetcode submit region end(Prohibit modification and deletion)
