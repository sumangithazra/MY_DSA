class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited=[[False]*m for _ in range(n)]
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            visited[r][c]=True
            for dr, dc in direction:
                new_r=r+dr
                new_c=c+dc
                if 0<=new_r<n and 0<=new_c<m and not visited[new_r][new_c] and grid[new_r][new_c]==1:
                    dfs(new_r,new_c)
        for r in range(n):
            if not visited[r][0] and grid[r][0]==1:
                dfs(r,0)
            if not visited[r][m-1] and grid[r][m-1]==1:
                dfs(r,m-1)
        for c in range(m):
            if not visited[0][c] and grid[0][c]==1:
                dfs(0,c)
            if not visited[n-1][c] and grid[n-1][c]==1:
                dfs(n-1,c)
        count=0
        for r in range(n):
            for c in range(m):
                if not visited[r][c] and grid[r][c]==1:
                    count+=1
        return count
        