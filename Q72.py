class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
            
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.vertices = set()
        for edge in edges:
            self.vertices.add(edge[0])
            self.vertices.add(edge[1])
        self.num_vertices = len(self.vertices)
        
    def kruskal_mst(self):
        disjoint_set = DisjointSet(self.num_vertices)
        self.edges.sort(key=lambda x: x[2])
        mst = []
        for edge in self.edges:
            if disjoint_set.find(edge[0]) != disjoint_set.find(edge[1]):
                mst.append(edge)
                disjoint_set.union(edge[0], edge[1])
        return mst
