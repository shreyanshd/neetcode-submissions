class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DisjointSet(n)
        components = n
        for u, v in edges:
            if ds.union(u, v):
                components -= 1
        return components


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, node):
        curr = node
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True
    
