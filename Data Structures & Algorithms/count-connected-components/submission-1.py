class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { i:[] for i in range(n) }
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visit = set()
        def dfs(i):
            if i in visit:
                return 
            
            visit.add(i)
            for j in graph[i]:
                dfs(j)
        
        components = 0
        for i in range(n):
            if i not in visit:
                components += 1
                dfs(i)
        
        return components
