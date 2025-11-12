from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        disc=[-1]*n
        low=[-1]*n
        bridges=[]
        self.timer=0
        def dfs(node,parent):
            disc[node]=self.timer
            low[node]=self.timer
            self.timer+=1
            for u in graph[node]:
                if u==parent:
                    continue
                if disc[u]==-1:
                    dfs(u,node)
                    low[node]=min(low[u],low[node])
                    if low[u]>disc[node]:
                        bridges.append([node,u])
                else:
                    low[node]=min(low[node],low[u])
        dfs(0,-1)
        return bridges


        