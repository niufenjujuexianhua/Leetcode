# Design a stack which supports the following operations. 
# 
#  Implement the CustomStack class: 
# 
#  
#  CustomStack(int maxSize) Initializes the object with maxSize which is the max
# imum number of elements in the stack or do nothing if the stack reached the maxS
# ize. 
#  void push(int x) Adds x to the top of the stack if the stack hasn't reached t
# he maxSize. 
#  int pop() Pops and returns the top of stack or -1 if the stack is empty. 
#  void inc(int k, int val) Increments the bottom k elements of the stack by val
# . If there are less than k elements in the stack, just increment all the element
# s in the stack. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["CustomStack","push","push","pop","push","push","push","increment","increment
# ","pop","pop","pop","pop"]
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
# Output
# [null,null,null,2,null,null,null,null,null,103,202,201,-1]
# Explanation
# CustomStack customStack = new CustomStack(3); // Stack is Empty []
# customStack.push(1);                          // stack becomes [1]
# customStack.push(2);                          // stack becomes [1, 2]
# customStack.pop();                            // return 2 --> Return top of th
# e stack 2, stack becomes [1]
# customStack.push(2);                          // stack becomes [1, 2]
# customStack.push(3);                          // stack becomes [1, 2, 3]
# customStack.push(4);                          // stack still [1, 2, 3], Don't 
# add another elements as size is 4
# customStack.increment(5, 100);                // stack becomes [101, 102, 103]
# 
# customStack.increment(2, 100);                // stack becomes [201, 202, 103]
# 
# customStack.pop();                            // return 103 --> Return top of 
# the stack 103, stack becomes [201, 202]
# customStack.pop();                            // return 202 --> Return top of 
# the stack 102, stack becomes [201]
# customStack.pop();                            // return 201 --> Return top of 
# the stack 101, stack becomes []
# customStack.pop();                            // return -1 --> Stack is empty 
# return -1.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= maxSize <= 1000 
#  1 <= x <= 1000 
#  1 <= k <= 1000 
#  0 <= val <= 100 
#  At most 1000 calls will be made to each method of increment, push and pop eac
# h separately. 
#  Related Topics Stack Design 
#  👍 564 👎 48


# leetcode submit region begin(Prohibit modification and deletion)
class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.st = []
        self.inc = []
        self.maxSize = maxSize
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.st) < self.maxSize:
            self.st.append(x)
            self.inc.append(0)


    def pop(self):
        """
        :rtype: int
        """
        if self.st:
            if len(self.st) >= 2:
                self.inc[-2] += self.inc[-1]
            return self.st.pop() + self.inc.pop()
        return -1

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# leetcode submit region end(Prohibit modification and deletion)
