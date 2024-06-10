import random
from Functions import selection, crossover, mutation

# Função para gerar cromossomos
def generate_chromosome(size, genes):
	chromosome = []
	for _ in range(size):
		chromosome.append(random.choice(genes))
	return chromosome

# Função para gerar a população de cromossomos
def generate_population(population_size, chromosome_size, genes):
	population = []
	for _ in range(population_size):
		chromosome = generate_chromosome(chromosome_size, genes)
		population.append(chromosome)
	return population

def new_generation(old_population, price, necessity, max_budget, chromosome_size, crossover_rate, mutation_rate):
	new_population = []

	while len(new_population) < len(old_population):

		# Primeiramente, fazemos a seleção dos pais
		parents = selection.select_chromosomes(old_population, price, necessity, max_budget)

		# Depois, fazemos o crossover dos pais para gerar os filhos
		children = crossover.crossover(parents, chromosome_size, crossover_rate)

		# Por fim, fazemos a mutação nos filhos gerados
		mutation.mutation(children[0], mutation_rate)
		mutation.mutation(children[1], mutation_rate)

		new_population.append(children[0])
		new_population.append(children[1])
	
	return new_population