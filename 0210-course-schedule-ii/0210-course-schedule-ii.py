from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''graph={i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited=[0]*numCourses
        order=[]
        def dfs(i):
            if visited[i]==1:
                return True
            if visited[i]==2:
                return False
            visited[i]=1
            for node in graph[i]:
                if dfs(node):
                    return True
            visited[i]=2
            order.append(i)
            return False
            
        for i in range(numCourses):
            if visited[i]==0:
                if dfs(i):
                    return []
        return order[::-1]'''
        graph={i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        indegree=[0]*numCourses
        for first,second in prerequisites:
            indegree[first]+=1
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        ans=[]
        while queue:
            item=queue.popleft()
            ans.append(item)
            for i in graph[item]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        if len(ans)!=numCourses:
            return []
        return ans
            