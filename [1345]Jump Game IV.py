# Given an array of integers arr, you are initially positioned at the first inde
# x of the array. 
# 
#  In one step you can jump from index i to index: 
# 
#  
#  i + 1 where: i + 1 < arr.length. 
#  i - 1 where: i - 1 >= 0. 
#  j where: arr[i] == arr[j] and i != j. 
#  
# 
#  Return the minimum number of steps to reach the last index of the array. 
# 
#  Notice that you can not jump outside of the array at any time. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that in
# dex 9 is the last index of the array.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You don't need to jump.
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index
#  of the array.
#  
# 
#  Example 4: 
# 
#  
# Input: arr = [6,1,9]
# Output: 2
#  
# 
#  Example 5: 
# 
#  
# Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 5 * 104 
#  -108 <= arr[i] <= 108 
#  
#  Related Topics Breadth-first Search 
#  👍 540 👎 42


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        import collections
        n = len(arr)
        if n <= 1:
            return 0

        dt = collections.defaultdict(set)
        for i, a in enumerate(arr):
            dt[a].add(i)

        fd, bd, seen = set([0]), set([n - 1]), set([0, n - 1])
        step = 0
        while fd and bd:
            if len(fd) > len(bd):
                fd, bd = bd, fd
            nxtlevel = set()

            for i in fd:
                for ni in set([i - 1, i + 1]).union(dt[arr[i]]):
                    if ni in bd:
                        return step + 1
                    if 0 <= ni < n and ni not in seen:
                        seen.add(ni)
                        nxtlevel.add(ni)

            step += 1
            fd = nxtlevel

# print(Solution().minJumps([100,-23,-23,404,100,23,23,23,3,404]))
# leetcode submit region end(Prohibit modification and deletion)
