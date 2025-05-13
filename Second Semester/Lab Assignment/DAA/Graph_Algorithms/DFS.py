def dfs(graph, v, visited):
    visited[v] = 1
    print(f"Visited: {v}")

    for w in graph[v]:
        if visited[w] == 0:
            dfs(graph, w, visited) #Recursive Call


#Undirected graph implemented using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = {v: 0 for v in graph}  # 0 means not visited

print("DFS Traversal starting from vertex A:")
dfs(graph, 'A', visited)
