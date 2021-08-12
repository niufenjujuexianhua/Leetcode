class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        U = L = 0
        D, R = len(matrix), len(matrix[0])
        i = j = di = 0

        res = []
        while len(res) < m * n:
            if di == 0:
                for j in range(L, R):
                    res.append(matrix[i][j])
                U += 1
            elif di == 1:
                for i in range(U, D):
                    res.append(matrix[i][j])
                R -= 1
            elif di == 2:
                for j in reversed(range(L, R)):
                    res.append(matrix[i][j])
                D -= 1
            else:
                for i in reversed(range(U, D)):
                    res.append(matrix[i][j])
                L += 1
            di = (di + 1) % 4 
        return res 