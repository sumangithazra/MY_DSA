import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        dist=[float('inf')]*(n+1)
        dist[k]=0
        pq=[(0,k)]
        while pq:
            curr_dist,node=heapq.heappop(pq)
            if curr_dist>dist[node]:
                continue
            for adjNode,wt in graph[node]:
                new_dist=dist[node]+wt
                if new_dist<dist[adjNode]:
                    dist[adjNode]=new_dist
                    heapq.heappush(pq,(new_dist,adjNode))
        Min_time=max(dist[1:])
        return -1 if Min_time==float('inf') else Min_time
        