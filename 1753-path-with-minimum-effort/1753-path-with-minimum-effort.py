import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n=len(heights)
        m=len(heights[0])
        efforts=[[float('inf')]*m for _ in range(n)]
        efforts[0][0]=0
        pq=[(0,0,0)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while pq:
            eff,r,c=heapq.heappop(pq)
            if r==n-1 and c==m-1: return eff
            if eff> efforts[r][c]: continue
            for dr,dc in directions:
                new_r=r+dr
                new_c=c+dc
                if 0<=new_r<n and 0<=new_c<m:
                    new_eff=max(eff,abs(heights[new_r][new_c]-heights[r][c]))
                    if new_eff<efforts[new_r][new_c]:
                        efforts[new_r][new_c]=new_eff
                        heapq.heappush(pq,(new_eff,new_r,new_c)) 
        return 0    