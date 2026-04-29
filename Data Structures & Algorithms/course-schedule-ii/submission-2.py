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
            if course in seen:
                return True
            
            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            order.append(course)
            seen.add(course)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        
        return order

        