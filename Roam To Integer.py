# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 18:15:35 2017

@author: twu
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M' : 1000}
        num = []

        while len(s) >= 2:
            if dictionary[s[-2]] < dictionary[s[-1]]:
                int = dictionary[s[-1]] - dictionary[s[-2]] 
                num.append(int)
                s = s[:-2]
            else:
                int = dictionary[s[-1]]
                num.append(int)
                s = s[:-1]

        for i in s:
            num.append(dictionary[i])
        num = sum(num)
        return num

        
class Solution2(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M' : 1000}
        num = 0
        for i in range(len(s)-1):
            if dictionary[s[i]] < dictionary[s[i+1]]:
                num -= dictionary[s[i]]
            else:
                num += dictionary[s[i]]

        return num + dictionary[s[-1]]


class Solution3(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

        res, p = 0, 'I'
        for c in s[::-1]:
            res, p = res - d[c] if d[c] < d[p] else res + d[c], c
        return res
            
if __name__ == '__main__':
    result = Solution3().romanToInt('DCXIX')
    print(result)
    
    
    
    