class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
        self.size=[1]*n
    def findUparent(self,node):
        if self.parent[node]!=node:
            self.parent[node]=self.findUparent(self.parent[node])
        return self.parent[node]
    def UnionByRank(self,u,v):
        pu=self.findUparent(u)
        pv=self.findUparent(v)
        if pu==pv:
            return
        if self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        elif self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1
    def UnionBySize(self,u,v):
        pu=self.findUparent(u)
        pv=self.findUparent(v)
        if pu==pv:
            return
        if self.size[pu]<self.size[pv]:
            self.parent[pu]=pv
            self.size[pv]+=self.size[pu]
        else:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dsu=DisjointSet(n*n)
        def index(r,c):
            return r*n + c 
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(n):
            for c in range(n):
                if  grid[r][c]==1:
                    for dr,dc in directions:
                        new_dr=r+dr
                        new_dc=c+dc
                        if 0<=new_dr<n and 0<=new_dc<n and grid[new_dr][new_dc]==1:
                            dsu.UnionBySize(index(r,c),index(new_dr,new_dc))
        maxland=0
        for r in range(n):
            for c in range(n):
                if grid[r][c]==0:
                    UniqueParent=set()
                    for dr,dc in directions:
                        new_dr=r+dr
                        new_dc=c+dc
                        if 0<=new_dr<n and 0<=new_dc<n and grid[new_dr][new_dc]==1:
                            UniqueParent.add(dsu.findUparent(index(new_dr,new_dc)))
                    new_size=1
                    for nodes in UniqueParent:
                        new_size+=dsu.size[nodes]
                    maxland=max(maxland,new_size)

        for i in range(n*n):
            if grid[i//n][i%n]==1:
                maxland=max(maxland,dsu.size[dsu.findUparent(i)])
        return maxland
