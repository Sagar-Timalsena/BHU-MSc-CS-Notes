def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node)  # Process the node
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
