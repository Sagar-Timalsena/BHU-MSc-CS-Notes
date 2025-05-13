def dijkstra(v, cost, n):
    DIST = [float('inf')] * n
    S = [0] * n

    for i in range(n):
        DIST[i] = cost[v][i]
        S[i] = 0

    DIST[v] = 0
    S[v] = 1

    for _ in range(n):
        # Choose u such that DIST[u] is minimum and S[u] == 0
        min_dist = float('inf')
        u = -1
        for j in range(n):
            if S[j] == 0 and DIST[j] < min_dist:
                min_dist = DIST[j]
                u = j

        if u == -1:  # No reachable vertex
            break

        S[u] = 1

        for w in range(n):
            if cost[u][w] != float('inf') and S[w] == 0:
                DIST[w] = min(DIST[w], DIST[u] + cost[u][w])

    return DIST

INF = float('inf')
cost_matrix = [
    [0,  4,  INF, INF, INF, 10],
    [INF, 0,  2, INF, INF, INF],
    [INF, INF, 0, 3, INF, INF],
    [INF, INF, INF, 0, 1, INF],
    [INF, INF, INF, INF, 0, 2],
    [INF, INF, INF, INF, INF, 0]
]

n = len(cost_matrix)
source = 0  # Starting from vertex 0

distances = dijkstra(source, cost_matrix, n)

print(f"Shortest distances from node {source}:")
for i, d in enumerate(distances):
    print(f"to node {i} = {d}")

