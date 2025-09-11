from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph={i: [] for i in range(n)}
        for u,des, prc in flights:
            graph[u].append((des,prc))
        dist=[float('inf')]*n
        dist[src]=0
        q=deque()
        q.append((0,src,0))
        while q:
            stop,node,dis=q.popleft()
            if stop>k: continue
            for dest,cost in graph[node]:
                if dis+cost<dist[dest]:
                    dist[dest]=dis+cost
                    q.append((stop+1,dest,dis+cost))
        if dist[dst]==float("inf"): return -1
        return dist[dst]
        
        