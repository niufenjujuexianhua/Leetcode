# Implement the RandomizedCollection class: 
# 
#  
#  RandomizedCollection() Initializes the RandomizedCollection object. 
#  bool insert(int val) Inserts an item val into the multiset if not present. Re
# turns true if the item was not present, false otherwise. 
#  bool remove(int val) Removes an item val from the multiset if present. Return
# s true if the item was present, false otherwise. Note that if val has multiple o
# ccurrences in the multiset, we only remove one of them. 
#  int getRandom() Returns a random element from the current multiset of element
# s (it's guaranteed that at least one element exists when this method is called).
#  The probability of each element being returned is linearly related to the numbe
# r of same values the multiset contains. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", 
# "getRandom"]
# [[], [1], [1], [2], [], [1], []]
# Output
# [null, true, false, true, 2, true, 1]
# 
# Explanation
# RandomizedCollection randomizedCollection = new RandomizedCollection();
# randomizedCollection.insert(1);   // return True. Inserts 1 to the collection.
#  Returns true as the collection did not contain 1.
# randomizedCollection.insert(1);   // return False. Inserts another 1 to the co
# llection. Returns false as the collection contained 1. Collection now contains [
# 1,1].
# randomizedCollection.insert(2);   // return True. Inserts 2 to the collection,
#  returns true. Collection now contains [1,1,2].
# randomizedCollection.getRandom(); // getRandom should return 1 with the probab
# ility 2/3, and returns 2 with the probability 1/3.
# randomizedCollection.remove(1);   // return True. Removes 1 from the collectio
# n, returns true. Collection now contains [1,2].
# randomizedCollection.getRandom(); // getRandom should return 1 and 2 both equa
# lly likely.
#  
# 
#  
#  Constraints: 
# 
#  
#  -231 <= val <= 231 - 1 
#  At most 105 calls will be made to insert, remove, and getRandom. 
#  There will be at least one element in the data structure when getRandom is ca
# lled. 
#  
# 
#  
# Follow up: Could you implement the functions of the class with each function w
# orks in average O(1) time? Related Topics Array Hash Table Design 
#  👍 1117 👎 91


# leetcode submit region begin(Prohibit modification and deletion)
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos, self.ls = collections.defaultdict(set), []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.pos[val].add(len(self.ls))
        self.ls.append(val)

        return len(self.pos[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.pos[val]:
            return False

        i = self.pos[val].pop()
        self.ls[i] = self.ls[-1]
        self.pos[self.ls[-1]].add(i)
        self.pos[self.ls[-1]].discard(len(self.ls) - 1)
        self.ls.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.ls)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)
