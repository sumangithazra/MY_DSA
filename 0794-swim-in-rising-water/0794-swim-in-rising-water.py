import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visited=[[False]*n for _ in range(n)]
        #(height or time, row, col)
        pq=[(grid[0][0],0,0)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        visited[0][0]=True
        while pq:
            time,r,c=heapq.heappop(pq)
            if r==n-1 and c==n-1:
                return time
            for dr,dc in directions:
                new_dr=r+dr
                new_dc=c+dc
                if 0<=new_dr<n and 0<=new_dc<n and not visited[new_dr][new_dc]:
                    visited[new_dr][new_dc]=True
                    new_time=max(time,grid[new_dr][new_dc])
                    heapq.heappush(pq,(new_time,new_dr,new_dc))
        return time

        