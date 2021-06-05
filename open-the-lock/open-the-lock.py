class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        bfs, step, seen = collections.deque(['0000']), 0, set(['0000'] + deadends)
        while bfs:
            size = len(bfs)
            for _ in range(size):
                node = bfs.popleft()

                if node == target:
                    return step
                if node in deadends:
                    continue 

                self.next(bfs, node, seen)
            step += 1
        return -1


    def next(self, bfs, node, seen):
        for i, d in enumerate(node):
            for dir in [-1, 1]:
                nnode = node[:i] + str((int(d) + dir) % 10) + node[i + 1:]
                if nnode not in seen:
                    bfs.append(nnode)
                    seen.add(nnode)