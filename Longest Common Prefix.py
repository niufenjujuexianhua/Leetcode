# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 16:39:51 2017

@author: twu

if need to loop through a list in both index and vlaue, use enumerate()
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
                
class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """                
        prefix = '';
        # * is the unpacking operator, essential here
        for z in zip(*strs):
            bag = set(z)
            if len(bag) == 1:
                prefix += bag.pop()
            else:
                break
        return prefix
        
         
class Solution3(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """           
        minL = min(map(len, strs)) if strs else 0
        for i in range(minL):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:minL] if minL else ""
        
                
        

      
if __name__ == '__main__':
    result = Solution3().longestCommonPrefix(['a', 'b'])
    print(result)
    
    
    