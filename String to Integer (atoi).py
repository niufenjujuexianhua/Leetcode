# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 20:59:02 2017

@author: twu
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ls = list(s.strip())
        if len(s) == 0 : return 0
        
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))
        
class Solution2(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        str = str.replace(' ', '')
        if str[0] == '-':
            sign = -1
            str = str[1:]

        for i,v in enumerate(str):
            if v not in '+-' and not v.isdigit():
                str = str[:i]
                break
        try:
            ret = int(str)
        except:
            return 0
        return max(min(ret*sign, 2**31-1), -2**31)
   
        
if __name__ == '__main__':
    result = Solution2().myAtoi('    ')
    print(result)