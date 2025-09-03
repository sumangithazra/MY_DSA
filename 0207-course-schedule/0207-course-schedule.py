from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        queue=deque()
        for node, prev in prerequisites:
            graph[prev].append(node)
        indegree=[0]*numCourses
        for first, second in prerequisites:
            indegree[first]+=1
        #print(indegree)
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        count=0
        while queue:
            elem=queue.popleft()
            for i in graph[elem]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
            count+=1
        if count==numCourses: return True
        return False
            
        