# Design a data structure to store the strings' count with the ability to return
#  the strings with minimum and maximum counts. 
# 
#  Implement the AllOne class: 
# 
#  
#  AllOne() Initializes the object of the data structure. 
#  inc(String key) Increments the count of the string key by 1. If key does not 
# exist in the data structure, insert it with count 1. 
#  dec(String key) Decrements the count of the string key by 1. If the count of 
# key is 0 after the decrement, remove it from the data structure. It is guarantee
# d that key exists in the data structure before the decrement. 
#  getMaxKey() Returns one of the keys with the maximal count. If no element exi
# sts, return an empty string "". 
#  getMinKey() Returns one of the keys with the minimum count. If no element exi
# sts, return an empty string "". 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMin
# Key"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# Output
# [null, null, null, "hello", "hello", null, "hello", "leet"]
# 
# Explanation
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "leet"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= key.length <= 10 
#  key consists of lowercase English letters. 
#  It is guaranteed that for each call to dec, key is existing in the data struc
# ture. 
#  At most 3 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey. 
#  
# 
#  
#  Follow up: Could you apply all the operations in O(1) time complexity? 
#  Related Topics Design 
#  👍 774 👎 94


# leetcode submit region begin(Prohibit modification and deletion)
class ListNode():
    def __init__(self, key, cnt):
        self.keys = set([key])
        self.cnt = cnt
        self.pre = self.next = None

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dt = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        cur = self.dt[key] if key in self.dt else self.head
        cur.keys.discard(key)

        if cur.cnt + 1 == cur.next.cnt:
            new = cur.next
        else:
            new = ListNode(key, cur.cnt + 1)
            self.insert(cur, new)

        self.dt[key] = new
        if not cur.keys and cur.cnt != 0:
            cur.pre.next, cur.next.pre = cur.next, cur.pre

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        cur = self.dt[key]
        cur.keys.discard(key)

        if cur.cnt - 1 == cur.pre.cnt:
            new = cur.pre
        else:
            new = ListNode(key, cur.cnt - 1)
            self.insert(cur.pre, new)

        self.dt[key] = new
        if not cur.keys and cur.cnt != 0:
            cur.pre.next, cur.next.pre = cur.next, cur.pre

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.tail.pre.cnt != 0:
            key = self.tail.pre.keys.pop()
            self.tail.pre.keys.add(key)
            return key
        return ''

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head.next.cnt != 0:
            key = self.head.next.keys.pop()
            self.head.next.keys.add(key)
            return key
        return ''

    def insert(self, pre, node):
        node.pre, node.next = pre, pre.next
        pre.next = node
        node.next.pre = node


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# leetcode submit region end(Prohibit modification and deletion)
