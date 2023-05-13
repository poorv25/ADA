import random

def max_cut(graph, max_iterations=1000):
    # Initialize the solution
    solution = [random.choice([0, 1]) for _ in range(len(graph))]
    
    # Iterate until the maximum number of iterations is reached
    for _ in range(max_iterations):
        # Choose a random vertex to flip
        vertex = random.randint(0, len(graph) - 1)
        
        # Compute the gain in the objective function by flipping the vertex
        gain = sum((1 - 2 * solution[vertex]) * graph[vertex][j] for j in range(len(graph)))
        
        # If the gain is positive, flip the vertex
        if gain > 0:
            solution[vertex] = 1 - solution[vertex]
    
    # Return the solution
    return solution
