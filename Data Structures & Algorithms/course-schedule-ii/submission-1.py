class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {n:[] for n in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        order = []
        seen = set()
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            graph[course] = []
            if course not in seen:
                order.append(course)
                seen.add(course)
            visited.remove(course)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        
        return order

        