import heapq

def dijkstra(graph, start):
    # Create a dictionary to store the distance to each vertex
    distances = {vertex: float('inf') for vertex in graph}
    # Set the distance to the start vertex to be 0
    distances[start] = 0
    # Create a priority queue and add the start vertex with distance 0
    queue = [(0, start)]
    # Create a dictionary to store the shortest path to each vertex
    path = {start: [start]}
    
    while queue:
        # Pop the vertex with the smallest distance from the queue
        current_distance, current_vertex = heapq.heappop(queue)
        # If the distance to this vertex is already greater than the stored distance, ignore it
        if current_distance > distances[current_vertex]:
            continue
        # Loop through the neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            # Calculate the distance to the neighbor via the current vertex
            distance = current_distance + weight
            # If the new distance is less than the stored distance, update the distances and path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = path[current_vertex] + [neighbor]
                # Add the neighbor to the queue with its new distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances, path
