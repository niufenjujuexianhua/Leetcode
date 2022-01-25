class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        import collections
        d= collections.defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                d[i+j].append(matrix[i][j])
        ans= []
        for entry in d.items():
            if entry[0] % 2 == 0:
                ans.extend(entry[1][::-1])
            else:
                ans.extend(entry[1])
        return ans