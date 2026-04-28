class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            
            prereqs = graph[course]
            if len(prereqs) == 0:
                return True
            
            visited.add(course)
            
            for prereq in prereqs:
                if not dfs(prereq):
                    return False
            
            prereqs = []
            graph[course] = prereqs
            visited.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

