# Design your implementation of the circular queue. The circular queue is a line
# ar data structure in which the operations are performed based on FIFO (First In 
# First Out) principle and the last position is connected back to the first positi
# on to make a circle. It is also called "Ring Buffer". 
# 
#  One of the benefits of the circular queue is that we can make use of the spac
# es in front of the queue. In a normal queue, once the queue becomes full, we can
# not insert the next element even if there is a space in front of the queue. But 
# using the circular queue, we can use the space to store new values. 
# 
#  Implementation the MyCircularQueue class: 
# 
#  
#  MyCircularQueue(k) Initializes the object with the size of the queue to be k.
#  
#  int Front() Gets the front item from the queue. If the queue is empty, return
#  -1. 
#  int Rear() Gets the last item from the queue. If the queue is empty, return -
# 1. 
#  boolean enQueue(int value) Inserts an element into the circular queue. Return
#  true if the operation is successful. 
#  boolean deQueue() Deletes an element from the circular queue. Return true if 
# the operation is successful. 
#  boolean isEmpty() Checks whether the circular queue is empty or not. 
#  boolean isFull() Checks whether the circular queue is full or not. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFul
# l", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 3, true, true, true, 4]
# 
# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= 1000 
#  0 <= value <= 1000 
#  At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, an
# d isFull. 
#  
# 
#  
# Follow up: Could you solve the problem without using the built-in queue? Relat
# ed Topics Design Queue 
#  👍 966 👎 130


# leetcode submit region begin(Prohibit modification and deletion)
class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.arr = [0] * k
        self.f = 0
        self.r = -1
        self.cnt = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return False
        self.r = (self.r + 1) % self.k
        self.arr[self.r] = value
        self.cnt += 1
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty(): return False
        self.f = (self.f + 1) % self.k
        self.cnt -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.arr[self.f]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.arr[self.r]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.cnt == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.cnt == self.k


    # Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# leetcode submit region end(Prohibit modification and deletion)
