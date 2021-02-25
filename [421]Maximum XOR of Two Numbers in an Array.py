# Given an integer array nums, return the maximum result of nums[i] XOR nums[j],
#  where 0 ≤ i ≤ j < n. 
# 
#  Follow up: Could you do this in O(n) runtime? 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28. 
# 
#  Example 2: 
# 
#  
# Input: nums = [0]
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [2,4]
# Output: 6
#  
# 
#  Example 4: 
# 
#  
# Input: nums = [8,10,2]
# Output: 10
#  
# 
#  Example 5: 
# 
#  
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 104 
#  0 <= nums[i] <= 231 - 1 
#  
#  Related Topics Bit Manipulation Trie 
#  👍 1926 👎 210


# leetcode submit region begin(Prohibit modification and deletion)

class Trie():
    def __init__(self):
        self.nxt = [None, None]

class Solution(object):
    def findMaximumXOR(self, nums):
        trie, res = Trie(), 0
        
        for n in nums:
            self.insert(trie, n)
            res = max(res, self.search(trie, n))
        return res 

    def insert(self, trie, n):
        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            if not trie.nxt[bit]:
                trie.nxt[bit] = Trie()
            trie = trie.nxt[bit]

    def search(self, trie, n):
            maxn = 0
            for i in range(31, -1, -1):
                bit = (n >> i) & 1
                if trie.nxt[not bit]:
                    maxn |= 1 << i
                    trie = trie.nxt[not bit]
                elif trie.nxt[bit]:
                    trie = trie.nxt[bit]
                else:
                    break
            return maxn


        # mask, maxn = 0, 0
        # for i in range(31, -1, -1):
        #     mask |= (1 << i)
        #
        #     cands = {mask & n for n in nums}
        #
        #     tmp = maxn | (1 << i)
        #     for cand in cands:
        #         if tmp ^ cand in cands:
        #             maxn = tmp
        #             break
        # return maxn
# leetcode submit region end(Prohibit modification and deletion)
