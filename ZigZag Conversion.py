"""
issue log:
        if len(s) <= 1:
            return s
        if the strig is 'AB' and numRows=1, will get a division by 0 error
        
        need to change it to:
            if numRows == 1:
                return s
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        num = 2*numRows-2
        
        if numRows == 1:
            return s
            
        rows = ['']*numRows
        for idx in range(len(s)):
            if idx % num <= numRows-1:
                rows[idx % num] += s[idx]
            else:
                rows[num - idx % num] += s[idx]
        
        return ''.join(rows)
        
        

if __name__ == '__main__': 
    result = Solution().convert("ab", 1)
    print(result)