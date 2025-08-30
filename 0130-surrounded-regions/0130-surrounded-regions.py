class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])
        visited=[[False]*m for _ in range(n)]
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            visited[r][c]=True
            for dr, dc in direction:
                new_r=r+dr
                new_c=c+dc
                if 0<=new_r<n and 0<=new_c<m and not visited[new_r][new_c] and board[new_r][new_c]=="O":
                    dfs(new_r,new_c)


        for c in range(m):
            if not visited[0][c] and board[0][c]=="O":
                dfs(0,c)
            if not visited[n-1][c] and board[n-1][c]=="O":
                dfs(n-1,c)
        for r in range(n):
            if not visited[r][0] and board[r][0]=="O":
                dfs(r,0)
            if not visited[r][m-1] and board[r][m-1]=="O":
                dfs(r,m-1)
        for r in range(n):
            for c in range(m):
                if visited[r][c]==False and board[r][c]=="O":
                    board[r][c]="X"