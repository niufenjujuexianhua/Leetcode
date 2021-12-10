class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        st = []
        prev = 0
        for job in logs:
            id, type, time = job.split(':')
            id, time = int(id), int(time)

            if type == 'end':
                res[st[-1]] += time - prev + 1
                prev = time + 1
                st.pop()
            else:
                if st:
                    res[st[-1]] += time - prev
                prev = time
                st.append(id)
        return res