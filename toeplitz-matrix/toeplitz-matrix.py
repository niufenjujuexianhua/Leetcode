class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        import collections
        m, n = len(matrix), len(matrix[0])
        dt = collections.defaultdict(set)
        for i in range(m):
            for j in range(n):
                if j - i in dt and matrix[i][j] != dt[j - i]:
                    return False
                dt[j - i] = matrix[i][j]
        return True
        