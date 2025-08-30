from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        queue=deque()
        distance=[[0]*m for _ in range(n)]

        visited=[[False]*m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                if mat[r][c]==0:
                    queue.append((r,c,0))
                    visited[r][c]=True
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            r,c,d=queue.popleft()
            distance[r][c]=d
            for dr,dc in direction:
                new_r=r+dr
                new_c=c+dc
                if 0<=new_r<n and 0<=new_c<m and not visited[new_r][new_c]:
                    visited[new_r][new_c]=True
                    queue.append((new_r,new_c,d+1))
        return distance

        