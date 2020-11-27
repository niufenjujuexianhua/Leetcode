# Given an array of integers A, find the sum of min(B), where B ranges over ever
# y (contiguous) subarray of A. 
# 
#  Since the answer may be large, return the answer modulo 10^9 + 7. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [
# 1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17. 
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 30000 
#  1 <= A[i] <= 30000 
#  
# 
#  
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,
# 2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [11,81,94,43,3]
# Output: 444
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 3 * 104 
#  1 <= arr[i] <= 3 * 104 
#  
#  Related Topics Array Stack 
#  👍 1597 👎 104
# st[i]i + 1   j

# 345xxxx9
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr = [0] + arr + [0]
        st, res = [], 0
        for j, a in enumerate(arr):
            while st and arr[st[-1]] > a:
                cur = st.pop()
                lt, rt = st[-1], j

                res += arr[cur] * (cur - lt) * (rt - cur)
            st.append(j)

        return res % (10**9 + 7)
    # 0xx3xx6
# print(Solution().sumSubarrayMins([3,1,2,4]))
# leetcode submit region end(Prohibit modification and deletion)
