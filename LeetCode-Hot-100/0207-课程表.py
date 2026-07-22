class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dist=[[] for _ in range(numCourses)]
        for x,y in prerequisites:
            dist[y].append(x)
        color=[0]*numCourses
        def dfs(x):
            color[x]=1
            for i in dist[x]:
                if color[i] == 1:
                    return True
                elif color[i]==0 and dfs(i):
                    return True
            color[x]=2
            return False
        for i in range(numCourses):
            if dfs(i):
                return False
        return True
