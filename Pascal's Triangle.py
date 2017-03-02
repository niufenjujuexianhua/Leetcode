class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        start = [[1],[1,1]]
        for i in range(2, numRows):
            start.append([1]*(i+1))
            for k in range(1, i):
                start[i][k] = start[i-1][k-1] + start[i-1][k]
            # start[i][0], start[i][i] = 1, 1
        return start

class Solution2(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []

        for i in range(numRows):
            curr = list(res[-1]) if len(res) else []

            for k in range(1, len(curr)):
                curr[k] = res[-1][k - 1] + res[-1][k]
            res.append(curr + [1])
        return res


if __name__ == '__main__':
    result = Solution2().generate(5)
    print(result)