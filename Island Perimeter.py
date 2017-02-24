class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        count = 0
        # return sum(sum(i) for i in grid)
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                for v in range(len(direction)):
                    x = i + direction[v][0]
                    y = k + direction[v][1]
                    if 0 <= x <= len(grid)-1 and 0 <= y <= len(grid[0])-1:
                        if grid[x][y] == 1 and grid[i][k] == 1:
                            count += 1

        return sum(sum(i) for i in grid)*4 - count



if __name__ == '__main__':
    result = Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
    print(result)
