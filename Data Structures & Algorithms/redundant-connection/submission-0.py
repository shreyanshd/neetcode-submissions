class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        ds = DisjointSet(n)
        for u, v in edges:
            if not ds.union(u, v):
                return [u,v]


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