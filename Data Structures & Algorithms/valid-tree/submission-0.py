class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = { i:[] for i in range(n) }
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for j in graph[i]:
                if j == prev:
                    continue
                if dfs(j, i) == False:
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
