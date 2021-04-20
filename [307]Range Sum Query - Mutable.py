# Given an array nums and two types of queries where you should update the value
#  of an index in the array, and retrieve the sum of a range in the array. 
# 
#  Implement the NumArray class: 
# 
#  
#  NumArray(int[] nums) initializes the object with the integer array nums. 
#  void update(int index, int val) updates the value of nums[index] to be val. 
#  int sumRange(int left, int right) returns the sum of the subarray nums[left, 
# right] (i.e., nums[left] + nums[left + 1], ..., nums[right]). 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]
# 
# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 9 = sum([1,3,5])
# numArray.update(1, 2);   // nums = [1,2,5]
# numArray.sumRange(0, 2); // return 8 = sum([1,2,5])
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  -100 <= nums[i] <= 100 
#  0 <= index < nums.length 
#  -100 <= val <= 100 
#  0 <= left <= right < nums.length 
#  At most 3 * 104 calls will be made to update and sumRange. 
#  
#  Related Topics Binary Indexed Tree Segment Tree 
#  👍 1779 👎 106


# leetcode submit region begin(Prohibit modification and deletion)
class Node():
    def __init__(self, s, e, val):
        self.s = s
        self.e = e
        self.val = val
        self.left = self.right = None

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.tree = self.buildTree(nums, 0, len(nums) - 1)

    def buildTree(self, nums, s, e):
        if s > e:
            return
        if s == e:
            return Node(s, e, nums[s])
        m = s + (e - s) // 2
        root = Node(s, e, 0)
        root.left = self.buildTree(nums, s, m)
        root.right = self.buildTree(nums, m + 1, e)
        root.val = root.left.val + root.right.val
        return root

    def updateTree(self, root, index, val):
        if root.s == root.e:
            root.val = val
            return

        m = root.s + (root.e - root.s) // 2
        if index <= m:
            self.updateTree(root.left, index, val)
        else:
            self.updateTree(root.right, index, val)
        root.val = root.left.val + root.right.val

    def query(self, root, lt, rt):
        if rt < root.s or lt > root.e:
            return 0
        if lt == root.s and rt == root.e:
            return root.val

        ans = 0
        m = root.s + (root.e - root.s) // 2
        if rt <= m:
            ans += self.query(root.left, lt, rt)
        elif lt > m:
            ans += self.query(root.right, lt, rt)
        else:
            ans += self.query(root.left, lt, m)
            ans += self.query(root.right, m + 1, rt)
        return ans


    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.updateTree(self.tree, index, val)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.query(self.tree, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)
