class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[int(1e8)]*n for _ in range(n)]
        for i in range(n):
            dist[i][i]=0
        for s,e,wt in edges:
            dist[s][e]=wt
            dist[e][s]=wt
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k]!=int(1e8) and dist[k][j]!=int(1e8):
                        dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        ans=-1
        mincount=int(1e8)
        for i in range(n):
            count=0
            for j in range(n):
                if dist[i][j]<=distanceThreshold:
                    count+=1
            if count<=mincount:
                ans=i
                mincount=count
        return ans
                
        