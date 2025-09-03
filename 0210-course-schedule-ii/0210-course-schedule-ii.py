class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={i:[] for i in range(numCourses)}
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
        return order[::-1]
        