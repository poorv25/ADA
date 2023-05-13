def knapsack_greedy(values, weights, capacity):
    # Initialize the total value and weight to 0
    total_value = 0
    total_weight = 0
    
    # Create a list of tuples containing the value-to-weight ratios and their index
    ratios = [(values[i]/weights[i], i) for i in range(len(values))]
    
    # Sort the items by their value-to-weight ratio in decreasing order
    ratios.sort(reverse=True)
    
    # Loop through the items and add them to the knapsack until it's full
    for ratio, i in ratios:
        if total_weight + weights[i] <= capacity:
            total_value += values[i]
            total_weight += weights[i]
    
    return total_value
