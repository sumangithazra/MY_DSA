from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        reverse_g=[[] for _ in range(n)]
        indegree=[0]*n
        for i in range(n):
            for j in graph[i]:
                reverse_g[j].append(i)
                indegree[i]+=1
        #print(reverse_g)
        queue=deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        safe_node=[]
        while queue:
            #print('hello')
            item=queue.popleft()
            safe_node.append(item)
            for i in reverse_g[item]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        return sorted(safe_node)
        

        
        