class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        need = set()

        for a in arr:
            if a in need:
                return True
            need.add(a * 2)
            if a % 2 == 0:
                need.add(a // 2)
        return False