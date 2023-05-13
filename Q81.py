from collections import deque

# function to perform BFS traversal
def bfs(graph, start, end):
    # initialize visited and queue
    visited = set()
    queue = deque([(start, [])])
    
    # loop till queue is empty
    while queue:
        # get the next vertex and path
        vertex, path = queue.popleft()
        # if the vertex is not visited
        if vertex not in visited:
            # mark it as visited
            visited.add(vertex)
            # add the vertex to the path
            path = path + [vertex]
            # if we have reached the end node, return the path
            if vertex == end:
                return path
            # loop over the neighbors of the current vertex
            for neighbor in graph[vertex]:
                # if the neighbor is not visited, add it to the queue
                if neighbor not in visited:
                    queue.append((neighbor, path))
    # if end node is not reachable from start node, return None
    return None
