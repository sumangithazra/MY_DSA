from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        queue=deque()
        visited=[[False]*m for _ in range(n)]
        fresh_count=0
        for r in range(n):
            for c in range(m):
                if grid[r][c]==2:
                    visited[r][c]=True
                    queue.append((r,c,0))
                elif grid[r][c]==1:
                    fresh_count+=1
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        time=0
        while queue:
            r,c,t=queue.popleft()
            time=max(time,t)
            for dr,dc in direction:
                new_r=r+dr
                new_c=c+dc
                if 0<=new_r<n and 0<=new_c<m and not visited[new_r][new_c] and grid[new_r][new_c]==1:
                    visited[new_r][new_c]=True
                    fresh_count-=1
                    queue.append((new_r,new_c,t+1))
        return time if fresh_count==0 else -1
        
        