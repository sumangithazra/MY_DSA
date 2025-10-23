class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        #dp=[[-1]*n for _ in range(m)]
        prev=[0]*n
        for i in range(m):
            curr=[0]*n
            for j in range(n):
                if obstacleGrid[i][j]==1: curr[j]=0
                elif i==0 and j==0: curr[j]=1
                else:
                    up=0
                    left=0
                    if i>0: up=prev[j]
                    if j>0: left=curr[j-1]
                    curr[j]=up+left
            prev=curr
        return prev[n-1]

        