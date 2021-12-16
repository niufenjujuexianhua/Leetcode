class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = [0] * len(rooms)

        self.dfs(rooms, seen, 0)
        return all(seen)


    def dfs(self, rooms, seen, i):
        seen[i] = 1

        for nxt in rooms[i]:
            if seen[nxt] == 0:
                self.dfs(rooms, seen, nxt)