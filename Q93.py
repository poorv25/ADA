import sys

def tsp(costs):
    n = len(costs)
    min_cost = sys.maxsize
    
    # Define a function to calculate the lower bound of a node
    def bound(costs, path):
        # Calculate the cost of the path so far
        lower_bound = sum(costs[path[i]][path[i+1]] for i in range(len(path) - 1))
        
        # Add the cost of the nearest neighbor to the end of the path
        last_city = path[-1]
        nearest_neighbor = min((costs[last_city][j], j) for j in range(n) if j not in path)[1]
        lower_bound += costs[last_city][nearest_neighbor]
        
        return lower_bound
    
    # Define a recursive function to explore the search space
    def explore(path, cost):
        nonlocal min_cost
        
        # If the path is complete, update the minimum cost
        if len(path) == n:
            cost += costs[path[-1]][path[0]]
            min_cost = min(min_cost, cost)
            return
        
        # Calculate the lower bound for each child node
        lower_bounds = [(bound(costs, path + [j]), j) for j in range(n) if j not in path]
        
        # Sort the child nodes by their lower bounds
        lower_bounds.sort()
        
        # Explore the child nodes in order of their lower bounds
        for lower_bound, j in lower_bounds:
            # If the lower bound is greater than the current minimum cost, prune the node
            if lower_bound >= min_cost:
                break
            
            # Otherwise, explore the node
            explore(path + [j], cost + costs[path[-1]][j])
    
    # Start exploring from node 0
    explore([0], 0)
    
    return min_cost
