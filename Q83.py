import heapq

def dijkstra(graph, start, end):
    # Create a priority queue and initialize it with the start node
    pq = [(0, start)]
    # Create a dictionary to keep track of the shortest distances from the start node to other nodes
    dist = {start: 0}
    # Create a dictionary to keep track of the previous node on the shortest path from start to each node
    prev = {}

    # Loop until the priority queue is empty
    while pq:
        # Pop the node with the smallest distance from the priority queue
        (cost, current) = heapq.heappop(pq)

        # If we have reached the end node, we can stop
        if current == end:
            break

        # Loop through the neighbors of the current node
        for neighbor, weight in graph[current].items():
            # Calculate the distance to the neighbor through the current node
            new_cost = dist[current] + weight

            # If this new distance is shorter than the current shortest distance to the neighbor,
            # update the shortest distance and the previous node
            if neighbor not in dist or new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                prev[neighbor] = current
                # Add the neighbor to the priority queue with its new shortest distance
                heapq.heappush(pq, (new_cost, neighbor))

    # If we did not find a path to the end node, return None
    if end not in prev:
        return None

    # Build the shortest path by backtracking from the end node to the start node
    path = [end]
    while path[-1] != start:
        path.append(prev[path[-1]])
    path.reverse()

    # Return the shortest path and its length
    return path, dist[end]
