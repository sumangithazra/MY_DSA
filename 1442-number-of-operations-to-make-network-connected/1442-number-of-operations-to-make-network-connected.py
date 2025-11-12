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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        dsu=DisjointSet(n)
        for u,v in connections:
            dsu.UnionByRank(u,v)
        components=len(set(dsu.findUparent(i) for i in range(n)))
        return components-1            
        