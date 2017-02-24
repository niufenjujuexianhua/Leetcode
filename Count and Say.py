# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 23:21:07 2017

@author: twu
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        oldstr = "1"
        for _ in range(n - 1):
            l, r, lstr, newstr = 0, 0, len(oldstr), ""
            while r < lstr:
                while r < lstr and oldstr[r] == oldstr[l]:
                    r += 1
                newstr += str(r - l) + str(oldstr[l])
                l = r
            oldstr = newstr
        return oldstr

class Solution2(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        oldstr = "1"
        for i in range(n - 1):
            tmp = ''
            count = 1
            for j in range(1, len(oldstr) + 1):
                if j < len(oldstr) and oldstr[j] == oldstr[j - 1]:
                    count += 1
                else:
                    tmp += str(count) + oldstr[j - 1]
                    count = 1
            oldstr = tmp
        return oldstr

    
        
if __name__ == '__main__':
    result = Solution2().countAndSay(4)
    print(result)