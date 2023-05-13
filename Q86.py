import heapq
from collections import defaultdict

def prim(graph, start):
    visited = set([start])
    edges = [
        (cost, start, to) 
        for to, cost in graph[start].items()
    ]
    heapq.heapify(edges)
    mst_cost = 0
    mst_edges = []

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst_cost += cost
            mst_edges.append((frm, to))
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst_cost, mst_edges
