from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        queue=deque()
        if grid[0][0]==1 or grid[n-1][n-1]==1: return -1
        queue.append((0,0,1))
        visited=set()
        visited.add((0,0))
        directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        while queue:
            r,c,dist=queue.popleft()
            if r==n-1 and c==n-1:
                return dist
            for dr,dc in directions:
                new_r=r+dr
                new_c=c+dc
                if 0<=new_r<n and 0<=new_c<n and grid[new_r][new_c]==0 and (new_r,new_c) not in visited:
                    visited.add((new_r,new_c))
                    queue.append((new_r,new_c,dist+1))
        return -1



        