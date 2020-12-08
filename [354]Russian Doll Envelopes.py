# You have a number of envelopes with widths and heights given as a pair of inte
# gers (w, h). One envelope can fit into another if and only if both the width and
#  height of one envelope is greater than the width and height of the other envelo
# pe. 
# 
#  What is the maximum number of envelopes can you Russian doll? (put one inside
#  other) 
# 
#  Note: 
# Rotation is not allowed. 
# 
#  Example: 
# 
#  
#  
# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3 
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] 
# => [5,4] => [6,7]).
#  
#  
#  Related Topics Binary Search Dynamic Programming 
#  👍 1420 👎 47


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes: return 0

        envelopes.sort(key = lambda x : (x[0], -x[1]))
        ls = []
        res = 0
        for en in envelopes:
            i = self.bs(ls, en[1])
            if i == len(ls):
                ls.append(en[1])
                res += 1
            else:
                ls[i] = en[1]
        return res

    def bs(self, ls, n):
        if not ls: return 0

        s, e = 0, len(ls) - 1
        while s + 1 < e:
            m = s + (e - s) // 2
            if ls[m] >= n:
                e = m
            else:
                s = m
        if ls[s] >= n:
            return s
        if ls[e] >= n:
            return e
        return len(ls)

        
# leetcode submit region end(Prohibit modification and deletion)
