class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        n = row * col
        root, lft, rgt = list(range(n)), [0] * n, [0] * n
        for i in range(col):
            for j in range(row):
                lft[i * row + j] = i
                rgt[i * row + j] = i

        def find(x):
            if x != root[x]: root[x] = find(root[x])
            return root[x]

        def union(x, y):
            a, b = find(x), find(y)
            if a != b: root[a] = b
            lft[b] = min(lft[b], lft[a])  # update leftmost and rightmost index of the new component.
            rgt[b] = max(rgt[b], rgt[a])

        seen = set()
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
        for i, cell in enumerate(cells):
            cx, cy = cell[0] - 1, cell[1] - 1
            for dx, dy in dirs:
                x, y = cx + dx, cy + dy
                if 0 <= x < row and 0 <= y < col and (x, y) in seen:
                    union(cy * row + cx, y * row + x)
                    new = find(y * row + x)
                    if lft[new] == 0 and rgt[new] == col - 1:
                        return i
            seen.add((cx, cy))
        return n
