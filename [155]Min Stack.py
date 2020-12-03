# Design a stack that supports push, pop, top, and retrieving the minimum elemen
# t in constant time. 
# 
#  
#  push(x) -- Push element x onto stack. 
#  pop() -- Removes the element on top of the stack. 
#  top() -- Get the top element. 
#  getMin() -- Retrieve the minimum element in the stack. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#  
# 
#  
#  Constraints: 
# 
#  
#  Methods pop, top and getMin operations will always be called on non-empty sta
# cks. 
#  
#  Related Topics Stack Design 
#  👍 4209 👎 389


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.st:
            self.st.append((x, x))
        else:
            mn = min(x, self.st[-1][1])
            self.st.append((x, mn))
        

    def pop(self):
        """
        :rtype: None
        """
        if self.st:
            self.st.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.st:
            return self.st[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.st:
            return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
