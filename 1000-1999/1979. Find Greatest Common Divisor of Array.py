import sys
from collections import deque

def calculate_tree_bias(N, edges):
    # Step 1: Build the adjacency list
    tree = [[] for _ in range(N + 1)]  # Using 1-based indexing

    for A, B in edges:
        tree[A].append(B)
        tree[B].append(A)  # Since it's an undirected tree

    # Step 2: BFS to compute depths
    queue = deque([(1, 0)])  # (node, depth)
    visited = set()
    visited.add(1)
    
    bias = 0
    
    while queue:
        node, depth = queue.popleft()
        bias += depth  # Add depth to bias

        for neighbor in tree[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))
    
    # Step 3: Print the total bias
    print(bias)

# Read input
N = int(sys.stdin.readline().strip())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N - 1)]
calculate_tree_bias(N, edges)