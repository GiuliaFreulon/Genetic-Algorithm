import random
from Functions import fitness

# A seleção dos pais é feita por roleta, onde o valor fitness de cada cromossomo o da vantagem de escolha
def select_chromosomes(population, price, necessity, max_budget):
    fitness_list = []
	
    for chromosome in population:
        fitness_list.append(fitness.fitness_function(chromosome, price, necessity, max_budget))
    
    if(sum(fitness_list) == 0):
        print("Fitness total igual a zero, tente novamente!")
        return 0
		
    for i in range(len(fitness_list)):
        fitness_list[i] = fitness_list[i]/sum(fitness_list)
	
    parent1 = random.choices(population, weights=fitness_list, k=1)[0]
    parent2 = random.choices(population, weights=fitness_list, k=1)[0]
	
    return parent1, parent2