import heapq
from collections import defaultdict
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=10**9 +7
        graph=defaultdict(list)
        for u,v,t in roads:
            graph[u].append((v,t))
            graph[v].append((u,t))
        ways=[0]*n
        dist=[float('inf')]*n
        dist[0]=0
        ways[0]=1
        pq=[(0,0)]
        while pq:
            curr_dist,node=heapq.heappop(pq)
            if curr_dist>dist[node]:
                continue
            for adjNode,wt in graph[node]:
                new_dist=dist[node]+wt
                if new_dist<dist[adjNode]:
                    dist[adjNode]=new_dist
                    ways[adjNode]=ways[node]
                    heapq.heappush(pq,(new_dist,adjNode))
                elif new_dist==dist[adjNode]:
                    ways[adjNode]=(ways[node]+ways[adjNode])%MOD
        return ways[n-1]%MOD
                

        