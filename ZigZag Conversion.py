"""
issue log:
        if len(s) <= 1:
            return s
        if the strig is 'AB' and numRows=1, will get a division by 0 error
        
        need to change it to:
            if numRows == 1:
                return s
                
        if possible, rewrite solution2. Many edge cases need to consider. for example, when numRows=2
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
        
class Solution2(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """     
        rows = [''] * numRows

        if numRows == 1:
            return s
            
        index = -1
        step = 1
        
        for i in range(len(s)):
            index += step
            
            if index == numRows:
                index -= 2
                step = -1
            

            elif index == -1:
                index = 1
                step = 1
            rows[index] += s[i]

        return ''.join(rows)
                

if __name__ == '__main__': 
    result = Solution2().convert("abcdef", 3)
    print(result)