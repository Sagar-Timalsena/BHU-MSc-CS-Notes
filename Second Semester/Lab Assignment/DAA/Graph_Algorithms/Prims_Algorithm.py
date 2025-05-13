import sys

def prims_algorithm(cost):
    n = len(cost)
    near = [0] * n
    t = []
    
    #Find the edge with minimum cost
    min_val = sys.maxsize
    k = l = -1
    for i in range(n):
        for j in range(n):
            if cost[i][j] < min_val:
                min_val = cost[i][j]
                k, l = i, j
    
    print(f"Initial minimum edge: ({k}, {l}) with cost {min_val}")
    
    t.append((k, l))
    min_cost = cost[k][l]
    
    #Initialize near[]
    for i in range(n):
        if cost[i][l] < cost[i][k]:
            near[i] = l
        else:
            near[i] = k
    near[k] = near[l] = -1  # -1 means included in MST
    
    #Repeat until MST has (n - 1) edges
    for _ in range(n - 2):
        min_val = sys.maxsize
        j = -1
        for i in range(n):
            if near[i] != -1 and cost[i][near[i]] < min_val:
                j = i
                min_val = cost[i][near[i]]
        t.append((j, near[j]))
        print(f"Selected edge: ({j}, {near[j]}) with cost {cost[j][near[j]]}")
        min_cost += cost[j][near[j]]
        near[j] = -1
        
        for i in range(n):
            if near[i] != -1 and cost[i][near[i]] > cost[i][j]:
                near[i] = j
    
    return t, min_cost


# Driver code with sample input (5-node graph)
cost_matrix = [
    [999, 2, 999, 6, 999],
    [2, 999, 3, 8, 5],
    [999, 3, 999, 999, 7],
    [6, 8, 999, 999, 9],
    [999, 5, 7, 9, 999]
]

edges, total_cost = prims_algorithm(cost_matrix)

print("\nEdges in the Minimum Spanning Tree:")
for u, v in edges:
    print(f"({u}, {v})")

print(f"\nTotal cost of MST: {total_cost}")
