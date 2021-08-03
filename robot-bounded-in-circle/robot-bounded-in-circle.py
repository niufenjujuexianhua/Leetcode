class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dirs = [[0, 1], [1, 0], [0, -1], [ -1, 0]]
        x = y = dir = 0
        for ins in instructions:
            if ins == 'G':
                x += dirs[dir][0]
                y += dirs[dir][1]
            elif ins == 'L':
                dir = (dir + 1) % 4
            else:
                dir = (dir + 3) % 4

        return (x == 0 and y == 0) or dir != 0