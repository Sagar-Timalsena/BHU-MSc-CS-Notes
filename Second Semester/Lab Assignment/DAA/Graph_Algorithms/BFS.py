from collections import deque

def bfs(graph, start_vertex):
    visited = {v: 0 for v in graph}  # 0 -> not visited / 1 -> visited
    queue = deque()

    visited[start_vertex] = 1
    queue.append(start_vertex)

    while queue:
        u = queue.popleft()
        print(f"Visited: {u}")

        for w in graph[u]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1

#Undirected graph implemented using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS Traversal starting from vertex A:")
bfs(graph, 'A')
