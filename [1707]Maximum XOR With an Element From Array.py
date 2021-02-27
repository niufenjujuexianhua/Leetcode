# You are given an array nums consisting of non-negative integers. You are also 
# given a queries array, where queries[i] = [xi, mi]. 
# 
#  The answer to the ith query is the maximum bitwise XOR value of xi and any el
# ement of nums that does not exceed mi. In other words, the answer is max(nums[j]
#  XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger t
# han mi, then the answer is -1. 
# 
#  Return an integer array answer where answer.length == queries.length and answ
# er[i] is the answer to the ith query. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# Output: [3,3,7]
# Explanation:
# 1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR
#  3 = 2. The larger of the two is 3.
# 2) 1 XOR 2 = 3.
# 3) 5 XOR 2 = 7.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# Output: [15,-1,5]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length, queries.length <= 105 
#  queries[i].length == 2 
#  0 <= nums[j], xi, mi <= 109 
#  
#  Related Topics Bit Manipulation Trie 
#  👍 162 👎 9


# leetcode submit region begin(Prohibit modification and deletion)
# class Trie():
#     def __init__(self):
#         self.dt = {}

class Solution(object):
    def maximizeXor(self, nums, queries):
        trie, res, i = {}, [-1] * len(queries), 0
        nums.sort()
        q = sorted([(m, x, idx) for idx, (x, m) in enumerate(queries)])
        for m, x, idx in q:
            while i < len(nums) and nums[i] <= m:
                self.insert(trie, nums[i])
                i += 1
            res[idx] = self.search(trie, x)
        return res

    def insert(self, trie, n):
        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            if bit not in trie:
                trie[bit] = {}
            trie = trie[bit]

    def search(self, trie, n):
        if not trie:
            return -1
        maxn = 0
        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            if bit ^ 1 in trie:
                maxn |= 1 << i
                trie = trie[bit ^ 1]
            elif bit in trie:
                trie = trie[bit]
            else:
                break
        return maxn
    #     dt = {}
    #     for n, _ in queries:
    #         for i in range(31, -1, -1):
    #             if 1 << i > n:
    #                 dt[n] = i
    #             else:
    #                 break
    #     return [self.mxor(nums, x, m, dt) for x, m in queries]
    #
    # def mxor(self, nums, x, m, dt):
    #     nn = {n for n in nums if n <= m}
    #     maxn = 0
    #     for i in range(dt[x], -1, -1):
    #         # nnt = set()
    #         bit = (x >> i) & 1
    #         # for n in nn:
    #         #     if ((n >> i) & 1) == (bit ^ 1):
    #         #         nnt.add(n)
    #         # nn = nnt
    #         nn = {n for n in nn if ((n >> i) & 1) == (bit ^ 1)}
    #         if nn:
    #             maxn |= (1 << i)
    #     return maxn

print(Solution().maximizeXor([5,2,4,6,6,3],
[[12,4],[8,1],[6,3]]))
# leetcode submit region end(Prohibit modification and deletion)
