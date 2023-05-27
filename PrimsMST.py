from collections import defaultdict
import heapq


def prim_mst(graph):
    # Initialize variables
    mst = []
    visited = set()
    start_node = next(iter(graph))  # Start from any node
    visited.add(start_node)
    edges = [
        (weight, start_node, next_node)
        for next_node, weight in graph[start_node]
    ]
    heapq.heapify(edges)

    # Main algorithm loop
    while edges:
        weight, src, dest = heapq.heappop(edges)
        if dest not in visited:
            visited.add(dest)
            mst.append((src, dest, weight))
            for next_node, next_weight in graph[dest]:
                if next_node not in visited:
                    heapq.heappush(edges, (next_weight, dest, next_node))

    return mst


# Example usage
graph = defaultdict(list)
# Add edges and their weights to the graph
graph[0].append((1, 2))
graph[0].append((2, 3))
graph[1].append((0, 2))
graph[1].append((2, 4))
graph[1].append((3, 1))
graph[2].append((0, 3))
graph[2].append((1, 4))
graph[2].append((3, 5))
graph[3].append((1, 1))
graph[3].append((2, 5))

mst = prim_mst(graph)

# Print the Minimum Spanning Tree
for src, dest, weight in mst:
    print(f"{src} -- {dest} \tWeight: {weight}")
