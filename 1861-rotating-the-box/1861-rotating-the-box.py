class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        m, n = len(box), len(box[0])

        for i in range(m):
            j = n - 1
            idx = j
            while j >= 0:
                if box[i][j] == '#':
                    box[i][idx], box[i][j] = box[i][j], box[i][idx]
                    idx -= 1
                elif box[i][j] == '*':
                    idx = j - 1
                j -= 1

        # nbox = list(zip(*box))
        return list(zip(*box[::-1]))