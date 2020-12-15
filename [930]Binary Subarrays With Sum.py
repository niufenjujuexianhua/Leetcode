# In an array A of 0s and 1s, how many non-empty subarrays have sum S? 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#  
# 
#  
# 
#  Note: 
# 
#  
#  A.length <= 30000 
#  0 <= S <= A.length 
#  A[i] is either 0 or 1. 
#  Related Topics Hash Table Two Pointers 
#  👍 654 👎 29


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        # cnt = collections.defaultdict(int)
        # cnt[0] = 1
        # psum = res = 0
        # for a in A:
        #     psum += a
        #     res += cnt[psum - S]
        #     cnt[psum] += 1
        # return res

        def cnt(S):
            if S < 0: return 0
            res = i = 0
            for j, a in enumerate(A):
                S -= a
                while S < 0:
                    S += A[i]
                    i += 1
                res += j - i + 1
            return res
        return cnt(S) - cnt(S - 1)
        
# leetcode submit region end(Prohibit modification and deletion)
