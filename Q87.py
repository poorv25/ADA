import random
import math

def tsp_greedy_local_search(cities, iterations):
    n = len(cities)
    visited = [False] * n
    path = [0] * (n+1)
    path[0] = path[n] = 0  # Start and end at city 0
    visited[0] = True
    total_distance = 0
    
    # Greedy approach
    for i in range(1, n):
        nearest = None
        for j in range(n):
            if not visited[j] and (nearest is None or cities[path[i-1]][j] < cities[path[i-1]][nearest]):
                nearest = j
        path[i] = nearest
        visited[nearest] = True
        total_distance += cities[path[i-1]][nearest]
    total_distance += cities[path[n-1]][0]
    
    # Local search heuristic
    for k in range(iterations):
        improved = False
        for i in range(1, n-1):
            for j in range(i+1, n):
                new_path = path[:]
                new_path[i:j+1] = reversed(new_path[i:j+1])
                new_distance = calculate_distance(cities, new_path)
                if new_distance < total_distance:
                    path = new_path
                    total_distance = new_distance
                    improved = True
        if not improved:
            break
    
    return path, total_distance

def calculate_distance(cities, path):
    n = len(path)
    distance = 0
    for i in range(1, n):
        distance += cities[path[i-1]][path[i]]
    return distance

# Example usage
cities = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
path, distance = tsp_greedy_local_search(cities, 100)
print("Path:", path)
print("Distance:", distance)
