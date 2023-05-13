from typing import List, Tuple

INF = float('inf')

def bellman_ford(graph: List[Tuple[int, int, int]], start: int) -> List[int]:
    
    n = len(set([u for u, _, _ in graph] + [v for _, v, _ in graph]))
    dist = [INF] * n
    dist[start] = 0

    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycles
    for u, v, w in graph:
        if dist[u] != INF and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return dist
