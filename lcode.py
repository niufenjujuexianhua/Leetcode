class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """

    def killProcess(self, pid, ppid, kill):
        # Write your code here
        graph = collections.defaultdict(set)
        for par, kid in zip(ppid, pid):
            graph[par].add(kid)

        res = []
        self.dfs(graph, kill, res)
        return res

    def dfs(self, graph, node, res):
        res.append(node)

        for kid in graph[node]:
            self.dfs(graph, kid, res)