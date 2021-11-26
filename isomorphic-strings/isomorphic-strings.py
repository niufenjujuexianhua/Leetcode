class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dt1 = {}
        dt2 = {}
        for a, b in zip(s, t):
            if a in dt1 and dt1[a] != b or b in dt2 and dt2[b] != a:
                return False 
            dt1[a] = b 
            dt2[b] = a 
        return True 
        