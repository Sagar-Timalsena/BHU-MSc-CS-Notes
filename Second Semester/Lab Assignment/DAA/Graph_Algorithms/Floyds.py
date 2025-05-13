def floyd(cost):
    n = len(cost)
    # Initialize the solution matrix same as the input cost matrix
    A = [row[:] for row in cost]

    #Check if it is cheaper to go from i->j via an intermediate node k
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]

    return A

# Example usage
INF = float('inf')
cost_matrix = [
    [0,   3,   INF, 5],
    [2,   0,   INF, 4],
    [INF, 1,   0,   INF],
    [INF, INF, 2,   0]
]

shortest_paths = floyd(cost_matrix)

# Print result
for row in shortest_paths:
    print(row)
