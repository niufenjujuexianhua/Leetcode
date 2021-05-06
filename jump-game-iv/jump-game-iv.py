class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dt = collections.defaultdict(list)
        for i, a in enumerate(arr):
            dt[a].append(i)
        bf = collections.deque([0])
        seen = set([0])
        step = 0
        while bf:
            size = len(bf)
            for _ in range(size):
                i = bf.popleft()
                if i == len(arr) - 1:
                    return step

                for j in [i - 1, i + 1] + dt[arr[i]]:
                    if 0 <= j < len(arr) and i != j and j not in seen:
                        seen.add(j)
                        bf.append(j)
                del dt[arr[i]]
            step += 1
        return