# A função fitness soma o preço e a necessidade totais de cada cromossomo
# A nota fitness é igual a zero caso o preço total passe do preço máximo
# Senão, a nota fitness é igual à necessidade total
def fitness_function(chromosome, price, necessity, max_budget):
    total_price = 0
    total_necessity = 0

    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_price += price[i]
            total_necessity += necessity[i]

    if total_price > max_budget:
        return 0
    
    return total_necessity

def avg_fitness(population, price, necessity, max_budget):
    fitness_list = []
	
    for chromosome in population:
        fitness_list.append(fitness_function(chromosome, price, necessity, max_budget))

    return sum(fitness_list)/len(fitness_list)

def best_fitness(population, price, necessity, max_budget):
    fitness_list = []
	
    for chromosome in population:
        fitness_list.append(fitness_function(chromosome, price, necessity, max_budget))

    best_fitness = max(fitness_list)
    best_chromosome = population[fitness_list.index(best_fitness)]
    
    return best_fitness, best_chromosome