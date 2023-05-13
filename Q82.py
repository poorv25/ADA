def dfs(graph, start, visited):
    visited.add(start)
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

def find_connected_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            component = dfs(graph, node, visited)
            components.append(component)
    return components
