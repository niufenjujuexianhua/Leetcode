class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        import collections
        n = len(matrix)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                rows[val].add(i)
                cols[val].add(j)

        for val in range(1, n + 1):
            if val not in rows or val not in cols:
                return False
            if len(rows[val]) != n or len(cols[val]) != n:
                return False
        return True