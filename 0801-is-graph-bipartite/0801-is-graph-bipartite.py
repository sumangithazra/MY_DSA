class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1 for _ in range(n)]
        visited=[False for _ in range(n)]
        def dfs(node,clr):
            visited[node]=True
            color[node]=clr
            for i in graph[node]:
                if not visited[i]:
                    if dfs(i,not clr)==False:
                        return False
                elif visited[i]==True and color[i]==clr:
                    return False
            return True
        for i in range(n):
            if not visited[i]:
                if dfs(i,0)==False:
                    return False
        return True
        