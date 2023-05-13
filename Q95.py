import random

def knapsack_genetic_algorithm(values, weights, max_weight, population_size=10, generations=100):
    # Define fitness function
    def fitness(individual):
        # Calculate total value and weight of the knapsack
        total_value = sum(values[i] for i in range(len(values)) if individual[i] == 1)
        total_weight = sum(weights[i] for i in range(len(weights)) if individual[i] == 1)
        
        # If the weight exceeds the max weight, return a fitness of 0
        if total_weight > max_weight:
            return 0
        
        # Otherwise, return the total value as the fitness score
        return total_value
    
    # Initialize population
    population = [[random.randint(0, 1) for i in range(len(values))] for j in range(population_size)]
    
    # Evolve population
    for generation in range(generations):
        # Evaluate fitness of each individual in the population
        fitness_scores = [fitness(individual) for individual in population]
        
        # Select parents for crossover using tournament selection
        parents = []
        for i in range(population_size):
            tournament = random.sample(range(population_size), 2)
            parent = population[tournament[0]] if fitness_scores[tournament[0]] > fitness_scores[tournament[1]] else population[tournament[1]]
            parents.append(parent)
        
        # Crossover parents to create new offspring
        offspring = []
        for i in range(population_size):
            parent1 = parents[random.randint(0, population_size - 1)]
            parent2 = parents[random.randint(0, population_size - 1)]
            crossover_point = random.randint(0, len(values) - 1)
            child = parent1[:crossover_point] + parent2[crossover_point:]
            offspring.append(child)
        
        # Mutate offspring
        for i in range(population_size):
            for j in range(len(values)):
                if random.random() < 0.1:
                    offspring[i][j] = 1 - offspring[i][j]
        
        # Replace population with new generation
        population = offspring
    
    # Find individual with highest fitness score in final population
    fitness_scores = [fitness(individual) for individual in population]
    max_fitness = max(fitness_scores)
    best_individual = population[fitness_scores.index(max_fitness)]
    
    # Calculate total value and weight of the knapsack for the best individual
    total_value = sum(values[i] for i in range(len(values)) if best_individual[i] == 1)
    total_weight = sum(weights[i] for i in range(len(weights)) if best_individual[i] == 1)
    
    return (best_individual, max_fitness, total_value, total_weight)
