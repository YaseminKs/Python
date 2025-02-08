import random

# Problem parameters
POP_SIZE = 10   # Population size
GENES = [i for i in range( 100 )]  # Possible gene values (0 to 99)
TARGET = 2500   # Target solution (we maximize f(x) = x^2)
MUTATION_RATE = 0.1

# Fitness function (maximize f(x) = x^2)
def fitness( x ):
    return x ** 2

# Generate a random individual
def create_individual():
    return random.choice( GENES )

# Create initial population
def create_population():
    return [create_individual() for _ in range( POP_SIZE )]

# Selection (Roulette Wheel Selection)
def select( population ):
    total_fitness = sum( fitness( ind ) for ind in population )
    pick = random.uniform( 0, total_fitness )
    current = 0
    for ind in population:
        current += fitness( ind )
        if current >= pick:
            return ind

# Crossover (Single-point crossover)
def crossover( parent1, parent2 ):
    return ( parent1 + parent2 ) // 2  # Average the two parents

# Mutation (Random mutation)
def mutate(ind):
    if random.random() < MUTATION_RATE:
        return random.choice( GENES )
    return ind

# Genetic Algorithm function
def genetic_algorithm():
    population = create_population()
    
    for generation in range( 100 ):  # Run for 100 generations
        population = sorted( population, key=fitness, reverse=True )
        if fitness( population[0] ) == TARGET:
            break  # Stop if solution found
        
        new_population = []
        for _ in range( POP_SIZE // 2 ):
            parent1 = select( population )
            parent2 = select( population )
            child1 = mutate( crossover( parent1, parent2 ) )
            child2 = mutate( crossover( parent1, parent2 ) )
            new_population.extend( [child1, child2] )
        
        population = new_population
        print( f"Generation { generation }: Best solution = { population[0] }, Fitness = { fitness( population[0] ) }" )

    return population[0]

# Run Genetic Algorithm
best_solution = genetic_algorithm()
print( "\nBest solution found:", best_solution, "with fitness:", fitness( best_solution ) )
