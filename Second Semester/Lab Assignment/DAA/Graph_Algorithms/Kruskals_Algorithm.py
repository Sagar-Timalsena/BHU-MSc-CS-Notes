from minHeap import MinHeap

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u]) #Path compression for faster root finding in future
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root != v_root:
            self.parent[v_root] = u_root

def kruskal(n, edge_list):
    min_heap = MinHeap()
    disjoint_set = DisjointSet(n)
    mst_edges = []
    min_cost = 0

    # Insert edges into heap as (cost, u, v)
    for (u, v, cost) in edge_list:
        min_heap.insert((cost, u, v)) #Keeping cost first to allow comparison of tuples

    count = 0
    while count < n - 1 and min_heap.heap:
        cost, u, v = min_heap.extract_min()
        set_u = disjoint_set.find(u)
        set_v = disjoint_set.find(v)

        if set_u != set_v:
            mst_edges.append((u, v, cost))
            min_cost += cost
            disjoint_set.union(set_u, set_v)
            count += 1

    if count != n - 1:
        print("No spanning tree")
        return None
    return min_cost, mst_edges

# Format: (u, v, cost)
edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 5, 6)
]

n = 6  # number of vertices
min_cost, mst = kruskal(n, edges)
print("Minimum Cost:", min_cost)
print("MST Edges:", mst)
